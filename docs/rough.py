from plotly.subplots import make_subplots
import plotly.graph_objects as go
def catplot(df, x):   
    # Create subplots
    fig = make_subplots(
       rows=1, cols=2,
       specs=[[{"type": "pie"}, {"type": "histogram"}]]
    )

    fig.add_trace(go.Pie(
            labels=df[x].value_counts().index,
            values=df[x].value_counts(),
            hole=0.0,
            pull=[0.1, 0],
            marker=dict( line=dict(color='#FFFFFF', width=2))
        ),row=1, col=1)

    
    fig.append_trace(go.Histogram(
       x=df_eda[(df_eda[x]) & (df_eda['Status'] == status)],
    nbinsx=2,
    ), row=1, col=2)
    layout = go.Layout(bargap=0.2, barmode='group',width=100)
    fig = go.Figure(data=data, layout=layout)
    fig.show()