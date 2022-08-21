from sdg.open_sdg import open_sdg_build

def my_indicator_alteration(indicator, context):
    # If the number of years is 2 or less, use a bar chart.
    if indicator.data.Year.nunique() <= 2:
        indicator.meta['graph_type'] = 'bar'
    return indicator

open_sdg_build(config='config_data.yml', alter_indicator=my_indicator_alteration)
