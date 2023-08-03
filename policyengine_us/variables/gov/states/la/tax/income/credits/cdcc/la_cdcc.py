from policyengine_us.model_api import *


class la_cdcc(Variable):
    value_type = float
    entity = TaxUnit
    label = "Louisiana Child and Dependent Care Credit"
    unit = USD
    definition_period = YEAR
    reference = "http://legis.la.gov/Legis/Law.aspx?d=101769"
    defined_for = StateCode.LA

    adds = ["la_cdcc_non_refundable", "la_cdcc_refundable"]
