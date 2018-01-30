#!/usr/bin/env python

# This is an automatically generated script to run your query
# to use it you will require the intermine python client.
# To install the client, run the following command from a terminal:
#
#     sudo easy_install intermine
#
# For further documentation you can visit:
#     http://intermine.readthedocs.org/en/latest/web-services/

# The following two lines will be needed in every python script:
from intermine.webservice import Service
service = Service("https://yeastmine.yeastgenome.org:443/yeastmine/service")

# Get a new query on the class (table) you will be querying:
query = service.new_query("Gene")

# The view specifies the output columns
query.add_view(
    "primaryIdentifier", "secondaryIdentifier", "sequence.length",
    "introns.length"
)

# Uncomment and edit the line below (the default) to select a custom sort order:
# query.add_sort_order("Gene.primaryIdentifier", "ASC")

# You can edit the constraint values below
query.add_constraint("status", "IS NULL", code = "G")
query.add_constraint("status", "=", "Active", code = "F")
query.add_constraint("qualifier", "IS NULL", code = "E")
query.add_constraint("qualifier", "!=", "Dubious", code = "D")
query.add_constraint("introns.status", "IS NULL", code = "I")
query.add_constraint("introns.status", "=", "Active", code = "H")
query.add_constraint("introns.primaryIdentifier", "IS NOT NULL", code = "B")
query.add_constraint("organism.name", "=", "Saccharomyces cerevisiae", code = "J")
query.add_constraint("featureType", "=", "ORF", code = "C")
query.add_constraint("secondaryIdentifier", "ONE OF", ["YFL039C", "YDL029W", "YML036W", "YBL059C-A", "YKL190W", "YLL050C", "YIL111W", "YNL130C", "YBL040C", "YMR292W", "YNL038W", "YDL125C", "YNL004W", "YDR367W", "YBL026W", "YGL226C-A", "YOR122C", "YPL031C", "YJL001W", "YHR001W-A", "YGR183C", "YDL082W", "YMR142C", "YKL006W", "YHL001W", "YIL133C", "YNL069C", "YKL180W", "YJL177W", "YOL120C", "YNL301C", "YBR084C-A", "YBL027W", "YMR242C", "YOR312C", "YBR191W", "YPL079W", "YLR061W", "YBL087C", "YER117W", "YOL127W", "YLR344W", "YGR034W", "YHR010W", "YDR471W", "YGL103W", "YFR031C-A", "YIL018W", "YGL030W", "YDL075W", "YLR406C", "YPL143W", "YOR234C", "YER056C-A", "YIL052C", "YDL191W", "YDL136W", "YMR194W", "YPL249C-A", "YLR185W", "YDR500C", "YJL189W", "YIL148W", "YKR094C", "YNL162W", "YHR141C", "YPR043W", "YJR094W-A", "YML073C", "YLR448W", "YPR187W", "YDL130W", "YGR214W", "YLR048W", "YOR293W", "YMR230W", "YDR025W", "YBR048W", "YDR064W", "YCR031C", "YMR143W", "YDL083C", "YML024W", "YDR447C", "YDR450W", "YML026C", "YOL121C", "YNL302C", "YKR057W", "YJL136C", "YGR118W", "YPR132W", "YER074W", "YIL069C", "YKL156W", "YHR021C", "YLR287C-A", "YOR182C", "YJR145C", "YHR203C", "YPL090C", "YBR181C", "YOR096W", "YNL096C", "YBR189W", "YOL048C", "YDR129C", "YPL218W", "YMR079W", "YGL137W", "YAL030W", "YML085C", "YDR092W", "YBR082C", "YDL064W", "YHR012W", "YPR028W"], code = "A")

# Your custom constraint logic is specified with the code below:
query.set_logic("B and C and (D or E) and (F or G) and (H or I) and J and J and J and J and J and J and J and A")

for row in query.rows():
    print(row["introns.location"])

