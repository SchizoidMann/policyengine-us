from policyengine_us.model_api import *


class mi_interest_dividends_capital_gains_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Michigan interest, dividends, and capital gains deduction"
    unit = USD
    definition_period = YEAR
    documentation = "Michigan interest, dividends, and capital gains deduction of qualifying age."
    reference = (
        "http://legislature.mi.gov/doc.aspx?mcl-206-30",  # (1)(p)
        "https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/2022/2022-IIT-Forms/BOOK_MI-1040.pdf#page=16",
    )
    defined_for = "mi_interest_dividends_capital_gains_deduction_eligible"

    def formula(tax_unit, period, parameters):
        p = parameters(
            period
        ).gov.states.mi.tax.income.deductions.interest_dividends_capital_gains

        # Core deduction based on filing status.
        filing_status = tax_unit("filing_status", period)
        person = tax_unit.members

        # Interest, Dividends, and Capital Gains Deduction for senior citizens
        income = add(tax_unit, period, p.income_types)
        # The maximum amount of the deduction will be reduced by the amount of the
        # deduction claimed for retirement or pension benefits under
        # subdivision (e) or a deduction claimed under subdivision (f)(i), (ii), (iv), or (v)
        reductions_pay = add(
            person,
            period,
            ["military_retirement_pay", "taxable_pension_income"],
        )
        elderly_disabled_credit = tax_unit("elderly_disabled_credit", period)

        is_head_or_spouse = person("is_tax_unit_head_or_spouse", period)

        reductions = tax_unit.sum(
            (reductions_pay + elderly_disabled_credit) * is_head_or_spouse
        )
        reduced_amount = max_(0, p.amount[filing_status] - reductions)

        return min_(reduced_amount, income)
