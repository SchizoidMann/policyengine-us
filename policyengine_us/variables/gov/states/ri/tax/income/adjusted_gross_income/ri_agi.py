from policyengine_us.model_api import *


class ri_agi(Variable):
    value_type = float
    entity = TaxUnit
    label = "RI AGI subtractions from federal AGI"
    unit = USD
    definition_period = YEAR
    reference = "https://tax.ri.gov/sites/g/files/xkgbur541/files/2022-12/2022%201041%20Schedule%20M_w.pdf"
    defined_for = StateCode.RI
    adds = ["adjusted_gross_income"]
    subtracts = ["ri_agi_subtractions"]
