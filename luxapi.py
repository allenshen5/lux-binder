code = '''# Processing Data with Altair
visdf = df[['Horsepower']]
import numpy as np
series = visdf['Horsepower'].dropna() 
counts,bin_edges = np.histogram(series,bins=10)
bin_center = np.mean(np.vstack([bin_edges[0:-1],bin_edges[1:]]), axis=0)
visdf = pd.DataFrame(np.array([bin_center,counts]).T,columns=['Horsepower', "Number of Records"])
# Plotting Histogram with Altair
import altair as alt
measure = vis.get_attr_by_data_model("measure",exclude_record=True)[0]
msr_attr = vis.get_attr_by_channel(measure.channel)[0]
x_min = vis.min_max['Horsepower'][0]
x_max = vis.min_max['Horsepower'][1]
x_range = abs(max(vis.data['Horsepower']) - 
min(vis.data['Horsepower']))
plot_range = abs(x_max - x_min)
markbar = x_range / plot_range * 12
chart = alt.Chart(visdf).mark_bar(size=markbar).encode(
alt.X('Horsepower', title='Horsepower (binned)',bin=alt.Bin(binned=True), type=msr_attr.data_type, axis=alt.Axis(labelOverlap=True), scale=alt.Scale(domain=(x_min, x_max))),
alt.Y("Number of Records", type="quantitative")
)
chart = chart.configure_title(fontWeight=500,fontSize=13,font="Helvetica Neue")
chart = chart.configure_axis(titleFontWeight=500,titleFontSize=11,titleFont="Helvetica Neue",
labelFontWeight=400,labelFontSize=9,labelFont="Helvetica Neue",labelColor="#505050")
chart = chart.configure_legend(titleFontWeight=500,titleFontSize=10,titleFont="Helvetica Neue",
labelFontWeight=400,labelFontSize=9,labelFont="Helvetica Neue")
chart = chart.properties(width=160,height=150)
chart
'''

def to_code(viz):
  return code
