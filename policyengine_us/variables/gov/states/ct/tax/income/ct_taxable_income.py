from policyengine_us.model_api import *


class ct_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "Connecticut taxable income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.CT
