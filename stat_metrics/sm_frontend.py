import streamlit as st
import pandas as pd
import plotly.express as px
from sm_backend import * 
# Allow user input for data analysis and calculation
st.set_page_config('Statistical Metrics',page_icon=':bar_chart:')
option = st.selectbox('Select Indicator',('Summary Statistics','Probability (Z-Score)'))
if option == 'Summary Statistics':
    nums = st.text_area('Enter numbers separated by " , " (comma):')
    process = st.button('Enter')
    if process:
        test = process_input(nums)
        print(test)
        
        if type(test) == list:
            st.subheader('Measures of central tendency')
            metrics = summary_stats(test)
            st.write('Mean:',str(metrics.mean))
            st.write('Mode:',str(metrics.mode))
            st.write('Meadian:',str(metrics.median))
            st.subheader('Measures of Dispersion')
            st.write('Variance:',str(metrics.variance))
            st.write('Standard Deviation',str(metrics.standard_dev))
            if len(test) >= 4:
                st.write('IQR 1:',str(metrics.quartile1))
                st.write('IQR 3:',str(metrics.quartile3))
                st.write('Interquantile Range:',str(metrics.iqrRange))
            st.write('Min:',str(metrics.minimum))
            st.write('Max:',str(metrics.maximum))
            disp_data = pd.DataFrame({"nums":test})
            fig1 = px.histogram(disp_data)
            fig1.update_layout(bargap=0.2)
            st.plotly_chart(fig1)
        else:
            st.write(test)

elif option == 'Probability (Z-Score)':
    var_x = st.number_input('Enter X')
    mean = st.number_input('Enter Mean')
    stdv = st.number_input('Enter Standard Deviation')
    process1 = st.button('Enter')
    if process1:
        if var_x and mean and stdv:
            prob = probability(var_x,mean,stdv)
            st.write('Z-Score:',str(prob.zscore))
            st.write(f'One tailed test (Negative) P(x<{var_x}):',str(prob.pvals[0]))
            st.write(f'One tailed test (Positive) P(x>{var_x}):',str(prob.pvals[1]))
            st.write('Two tailed test:',str(prob.pvals[2]))
        else:
            st.write('Enter valid data')