import pandas as pd
import streamlit as st
from PIL import Image
import warnings

warnings.filterwarnings("ignore")

image = Image.open('C:\\Users\\Hamza Tufail\\Downloads\\logo.png')

st.image(image, width=120)

st.title("EEPROM Data Analyser V1.01")

st.write("Suleiman Sarmad")

# try:
# dataset = st.file_uploader("upload file here", type=['trc'])
# if dataset is not None:
#   df = pd.read_csv(dataset, header=None, sep='\s+')
#  st.write(dataset)
# except:
#   st.write("Please load a file to continue...")

file = st.file_uploader("Upload", type=["trc"])
# st.write(file)
columns = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', '7', '8', '9', '10', '11', '12', '13']
df = pd.read_csv(file, header=None, names=columns, sep='\s+', error_bad_lines=False)

mask = df["col4"].str.contains("18FFFF20") | df["col4"].str.contains("18FFFF80") | \
       df["col4"].str.contains("18FFFF81") | df["col4"].str.contains("18FFFF82")
df = df[mask]

df343544 = pd.DataFrame(df)
df199 = df343544.reset_index(drop=True)

# st.write(df343544)

# st.write(df)

User_input = st.selectbox(
    'Please select the battery to be analysed',
    ('18FFFF20', '18FFFF80', '18FFFF81', '18FFFF82'))

if '18FFFF20' in User_input:
    # st.write(df[df.eq("18FFFF20").any(1)])
    df2 = df199.drop(df199.columns[[0, 1, 2, 3, 4]], axis=1)
    df3 = (df199[df199.eq("18FFFF20").any(1)])
    df4 = df3.drop(df3.columns[[0, 1, 2, 3, 4]], axis=1)
    df4.columns = ['dec1', 'dec2', 'dec3', 'dec4', 'dec5', 'dec6', 'dec7', 'dec8']
    df5 = df4[['dec1', 'dec2', 'dec3', 'dec4', 'dec5', 'dec6', 'dec7', 'dec8']].applymap(lambda n: int(n, 16))
    df5['Log Nmbr'] = range(1, len(df5) + 1)
    status1 = ((df5["Log Nmbr"] * 8) + 25)
    status = pd.DataFrame(status1)
    df6 = status.rename(columns={'Log Nmbr': 'statuscalc'})
    df7 = pd.concat([df5[['dec5']], df6], axis=1)
    df8 = pd.concat([df5[['Log Nmbr']], df7], axis=1)
    df9 = df8.drop(df8.columns[[2]], axis=1)
    df10 = df9[df9['Log Nmbr'].isin(status['Log Nmbr'])]
    df11 = df10.drop(df10.columns[[0]], axis=1)
    df12 = df11.rename(columns={'dec5': 'Status'})
    df13 = df5[df5['Log Nmbr'].isin(status['Log Nmbr'])]
    df14 = df13['Error_Flag'] = (df13['dec6'] * 65536) + (df13['dec7'] * 256) + (df13['dec8'])
    df15 = df13.drop(df13.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df16 = pd.concat([df12, df15], axis=1)
    df16['Log Number'] = range(1, len(df16) + 1)
    current1 = ((df5["Log Nmbr"] * 8) + 26)
    current = pd.DataFrame(current1)
    df17 = df5[df5['Log Nmbr'].isin(current['Log Nmbr'])]
    df17['Current'] = (df17['dec5'] * 256) + (df17['dec6'])
    df18 = df17.drop(df17.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df19 = df16.reset_index()
    df20 = df19.drop(df19.columns[[0]], axis=1)
    df21 = df18.reset_index()
    df22 = df21.drop(df21.columns[[0]], axis=1)
    df23 = pd.concat([df20, df22], axis=1)
    df24 = df23[['Log Number', 'Status', 'Error_Flag', 'Current']]
    nbr_cycle1 = ((df5["Log Nmbr"] * 8) + 26)
    nbr_cycle = pd.DataFrame(nbr_cycle1)
    df25 = df5[df5['Log Nmbr'].isin(nbr_cycle['Log Nmbr'])]
    df25['Nbr Cycle'] = (df25['dec1'] * 256) + (df25['dec2'])
    df26 = df25.drop(df25.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df27 = df26.reset_index()
    df28 = df27.drop(df27.columns[[0]], axis=1)
    df29 = pd.concat([df24, df28], axis=1)
    nbr_reset1 = ((df5["Log Nmbr"] * 8) + 26)
    nbr_reset = pd.DataFrame(nbr_reset1)
    df30 = df5[df5['Log Nmbr'].isin(nbr_reset['Log Nmbr'])]
    df30['Nbr Reset'] = (df30['dec3'] * 256) + (df30['dec4'])
    df31 = df30.drop(df30.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df32 = df31.reset_index()
    df33 = df32.drop(df32.columns[[0]], axis=1)
    df34 = pd.concat([df29, df33], axis=1)
    Avg_vol1 = ((df5["Log Nmbr"] * 8) + 26)
    avg_vol = pd.DataFrame(Avg_vol1)
    df35 = df5[df5['Log Nmbr'].isin(avg_vol['Log Nmbr'])]
    df35['Avg Vol'] = (df35['dec7'] * 256) + (df35['dec8'])
    df36 = df35.drop(df35.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df37 = df36.reset_index()
    df38 = df37.drop(df37.columns[[0]], axis=1)
    df39 = pd.concat([df34, df38], axis=1)
    timestamp1 = ((df5["Log Nmbr"] * 8) + 25)
    timestamp = pd.DataFrame(timestamp1)
    df40 = df5[df5['Log Nmbr'].isin(timestamp['Log Nmbr'])]
    df40['timestamp'] = (df40['dec1'] * 16777216) + (df40['dec2'] * 65536) + (df40['dec3'] * 256) + (df40['dec4'])
    df41 = df40.drop(df40.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df42 = df41.reset_index()
    df43 = df42.drop(df42.columns[[0]], axis=1)
    df44 = pd.concat([df39, df43], axis=1)
    vcellH1 = ((df5["Log Nmbr"] * 8) + 27)
    vcellH = pd.DataFrame(vcellH1)
    df45 = df5[df5['Log Nmbr'].isin(vcellH['Log Nmbr'])]
    df45['V Cell H'] = (df45['dec1'] * 256) + (df45['dec2'])
    df46 = df45.drop(df45.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df47 = df46.reset_index()
    df48 = df47.drop(df47.columns[[0]], axis=1)
    df49 = pd.concat([df44, df48], axis=1)
    soc1 = ((df5["Log Nmbr"] * 8) + 27)
    soc = pd.DataFrame(soc1)
    df50 = df5[df5['Log Nmbr'].isin(soc['Log Nmbr'])]
    df50['SOC'] = (df50['dec5'])
    df51 = df50.drop(df50.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df52 = df51.reset_index()
    df53 = df52.drop(df52.columns[[0]], axis=1)
    df54 = pd.concat([df49, df53], axis=1)
    Avg_temp1 = ((df5["Log Nmbr"] * 8) + 27)
    Avg_temp = pd.DataFrame(Avg_temp1)
    df55 = df5[df5['Log Nmbr'].isin(Avg_temp['Log Nmbr'])]
    df55['Avg Temp'] = (df55['dec6'] * 256) + (df55['dec7'])
    df56 = df55.drop(df55.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df57 = df56.reset_index()
    df58 = df57.drop(df57.columns[[0]], axis=1)
    df59 = pd.concat([df54, df58], axis=1)
    V_cellL1 = ((df5["Log Nmbr"] * 8) + 27)
    V_cellL = pd.DataFrame(V_cellL1)
    df60 = df5[df5['Log Nmbr'].isin(V_cellL['Log Nmbr'])]
    df60['V Cell L'] = (df60['dec3'] * 256) + (df60['dec4'])
    df61 = df60.drop(df60.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df62 = df61.reset_index()
    df63 = df62.drop(df62.columns[[0]], axis=1)
    df64 = pd.concat([df59, df63], axis=1)
    SOH1 = ((df5["Log Nmbr"] * 8) + 29)
    SOH = pd.DataFrame(SOH1)
    df65 = df5[df5['Log Nmbr'].isin(SOH['Log Nmbr'])]
    df65['SOH'] = (df65['dec8'])
    df66 = df65.drop(df65.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df67 = df66.reset_index()
    df68 = df67.drop(df67.columns[[0]], axis=1)
    df69 = pd.concat([df64, df68], axis=1)
    max_current = ((df5["Log Nmbr"] * 8) + 30)
    max_cur = pd.DataFrame(max_current)
    df70 = df5[df5['Log Nmbr'].isin(max_cur['Log Nmbr'])]
    df70['Max Current Seen'] = (df70['dec1'] * 256) + (df70['dec2'])
    df71 = df70.drop(df70.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df72 = df71.reset_index()
    df73 = df72.drop(df72.columns[[0]], axis=1)
    df74 = pd.concat([df69, df73], axis=1)
    min_current = ((df5["Log Nmbr"] * 8) + 30)
    min_cur = pd.DataFrame(min_current)
    df75 = df5[df5['Log Nmbr'].isin(min_cur['Log Nmbr'])]
    df75['Min Current Seen'] = (df75['dec3'] * 256) + (df75['dec4'])
    df76 = df75.drop(df75.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df77 = df76.reset_index()
    df78 = df77.drop(df77.columns[[0]], axis=1)
    df79 = pd.concat([df74, df78], axis=1)
    H_Vcell1 = ((df5["Log Nmbr"] * 8) + 30)
    H_Vcell = pd.DataFrame(H_Vcell1)
    df80 = df5[df5['Log Nmbr'].isin(H_Vcell['Log Nmbr'])]
    df80['Highest VCell Seen'] = (df80['dec5'] * 256) + (df80['dec6'])
    df81 = df80.drop(df80.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df82 = df81.reset_index()
    df83 = df82.drop(df82.columns[[0]], axis=1)
    df84 = pd.concat([df79, df83], axis=1)
    L_Vcell1 = ((df5["Log Nmbr"] * 8) + 30)
    L_cell = pd.DataFrame(L_Vcell1)
    df85 = df5[df5['Log Nmbr'].isin(L_cell['Log Nmbr'])]
    df85['Lowest VCell Seen'] = (df85['dec7'] * 256) + (df85['dec8'])
    df86 = df85.drop(df85.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df87 = df86.reset_index()
    df88 = df87.drop(df87.columns[[0]], axis=1)
    df89 = pd.concat([df84, df88], axis=1)
    max_temp1 = ((df5["Log Nmbr"] * 8) + 31)
    max_temp = pd.DataFrame(max_temp1)
    df90 = df5[df5['Log Nmbr'].isin(max_temp['Log Nmbr'])]
    df90['Max Temp Seen'] = (df90['dec1'] * 256) + (df90['dec2'])
    df91 = df90.drop(df90.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df92 = df91.reset_index()
    df93 = df92.drop(df92.columns[[0]], axis=1)
    df94 = pd.concat([df89, df93], axis=1)
    min_temp1 = ((df5["Log Nmbr"] * 8) + 31)
    min_temp = pd.DataFrame(min_temp1)
    df95 = df5[df5['Log Nmbr'].isin(min_temp['Log Nmbr'])]
    df95['Min Temp Seen'] = (df95['dec3'] * 256) + (df95['dec4'])
    df96 = df95.drop(df95.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df97 = df96.reset_index()
    df98 = df97.drop(df97.columns[[0]], axis=1)
    df99 = pd.concat([df94, df98], axis=1)
    time1 = ((df5["Log Nmbr"] * 8) + 31)
    time = pd.DataFrame(time1)
    df100 = df5[df5['Log Nmbr'].isin(time['Log Nmbr'])]
    df100['Time Between Charges'] = (df100['dec5'] * 256) + (df100['dec6'])
    df101 = df100.drop(df100.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df102 = df101.reset_index()
    df103 = df102.drop(df102.columns[[0]], axis=1)
    df104 = pd.concat([df99, df103], axis=1)
    turn1 = ((df5["Log Nmbr"] * 8) + 32)
    turn = pd.DataFrame(turn1)
    df105 = df5[df5['Log Nmbr'].isin(turn['Log Nmbr'])]
    df105['Turn On Off Code'] = (df105['dec3'] * 256) + (df105['dec4'])
    df106 = df105.drop(df105.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df107 = df106.reset_index()
    df108 = df107.drop(df107.columns[[0]], axis=1)
    df109 = pd.concat([df104, df108], axis=1)
    lastchg1 = ((df5["Log Nmbr"] * 8) + 31)
    lastchg1F = pd.DataFrame(lastchg1)
    df110 = df5[df5['Log Nmbr'].isin(lastchg1F['Log Nmbr'])]
    df110['chg1'] = (df110['dec7'] * 16777216) + (df110['dec8'] * 65536)
    df111 = df110.drop(df110.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df112 = df111.reset_index()
    df113 = df112.drop(df112.columns[[0]], axis=1)
    lastchg2 = ((df5["Log Nmbr"] * 8) + 32)
    lastchg1G = pd.DataFrame(lastchg2)
    df114 = df5[df5['Log Nmbr'].isin(lastchg1G['Log Nmbr'])]
    df114['chg2'] = (df114['dec1'] * 256) + (df114['dec2'])
    df115 = df114.drop(df114.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df116 = df115.reset_index()
    df117 = df116.drop(df116.columns[[0]], axis=1)
    df117['Last Charge'] = (df113['chg1']) + (df117['chg2'])
    df118 = df117.drop(df117.columns[[0]], axis=1)
    df119 = pd.concat([df109, df118], axis=1)
    df120 = df119.assign(Capacity=None, Impedance=None)
    df121 = df120[
        ['Log Number', 'timestamp', 'Status', 'Error_Flag', 'Nbr Cycle', 'Nbr Reset', 'Current', 'Avg Vol', 'V Cell H',
         'V Cell L', 'SOC', 'Avg Temp', 'Impedance', 'Capacity', 'SOH', 'Max Current Seen', 'Min Current Seen',
         'Highest VCell Seen', 'Lowest VCell Seen', 'Max Temp Seen', 'Min Temp Seen', 'Time Between Charges',
         'Last Charge',
         'Turn On Off Code']]
    # with pd.ExcelWriter('C:\\Users\\Hamza Tufail\\Desktop\\sully\\EEPROMAnalyser.xlsx') as writer:
    # df4.to_excel(writer, sheet_name='EEPROM Decimal', index=False)
    # df109.to_excel(writer, sheet_name='Cyclic Data Raw', index=False)
    df = df121


    @st.experimental_memo
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')


    csv = convert_df(df)

    st.download_button(
        "Click to Download",
        csv,
        "Cyclic Data Raw.csv",
        "text/csv",
        key='download-csv'
    )

if '18FFFF80' in User_input:
    df2 = df199.drop(df.columns[[0, 1, 2, 3, 4]], axis=1)
    df3 = (df199[df199.eq("18FFFF80").any(1)])
    df4 = df3.drop(df3.columns[[0, 1, 2, 3, 4]], axis=1)
    df4.columns = ['dec1', 'dec2', 'dec3', 'dec4', 'dec5', 'dec6', 'dec7', 'dec8']
    df5 = df4[['dec1', 'dec2', 'dec3', 'dec4', 'dec5', 'dec6', 'dec7', 'dec8']].applymap(lambda n: int(n, 16))
    df5['Log Nmbr'] = range(1, len(df5) + 1)
    status1 = ((df5["Log Nmbr"] * 8) + 25)
    status = pd.DataFrame(status1)
    df6 = status.rename(columns={'Log Nmbr': 'statuscalc'})
    df7 = pd.concat([df5[['dec5']], df6], axis=1)
    df8 = pd.concat([df5[['Log Nmbr']], df7], axis=1)
    df9 = df8.drop(df8.columns[[2]], axis=1)
    df10 = df9[df9['Log Nmbr'].isin(status['Log Nmbr'])]
    df11 = df10.drop(df10.columns[[0]], axis=1)
    df12 = df11.rename(columns={'dec5': 'Status'})
    df13 = df5[df5['Log Nmbr'].isin(status['Log Nmbr'])]
    df14 = df13['Error_Flag'] = (df13['dec6'] * 65536) + (df13['dec7'] * 256) + (df13['dec8'])
    df15 = df13.drop(df13.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df16 = pd.concat([df12, df15], axis=1)
    df16['Log Number'] = range(1, len(df16) + 1)
    current1 = ((df5["Log Nmbr"] * 8) + 26)
    current = pd.DataFrame(current1)
    df17 = df5[df5['Log Nmbr'].isin(current['Log Nmbr'])]
    df17['Current'] = (df17['dec5'] * 256) + (df17['dec6'])
    df18 = df17.drop(df17.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df19 = df16.reset_index()
    df20 = df19.drop(df19.columns[[0]], axis=1)
    df21 = df18.reset_index()
    df22 = df21.drop(df21.columns[[0]], axis=1)
    df23 = pd.concat([df20, df22], axis=1)
    df24 = df23[['Log Number', 'Status', 'Error_Flag', 'Current']]
    nbr_cycle1 = ((df5["Log Nmbr"] * 8) + 26)
    nbr_cycle = pd.DataFrame(nbr_cycle1)
    df25 = df5[df5['Log Nmbr'].isin(nbr_cycle['Log Nmbr'])]
    df25['Nbr Cycle'] = (df25['dec1'] * 256) + (df25['dec2'])
    df26 = df25.drop(df25.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df27 = df26.reset_index()
    df28 = df27.drop(df27.columns[[0]], axis=1)
    df29 = pd.concat([df24, df28], axis=1)
    nbr_reset1 = ((df5["Log Nmbr"] * 8) + 26)
    nbr_reset = pd.DataFrame(nbr_reset1)
    df30 = df5[df5['Log Nmbr'].isin(nbr_reset['Log Nmbr'])]
    df30['Nbr Reset'] = (df30['dec3'] * 256) + (df30['dec4'])
    df31 = df30.drop(df30.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df32 = df31.reset_index()
    df33 = df32.drop(df32.columns[[0]], axis=1)
    df34 = pd.concat([df29, df33], axis=1)
    Avg_vol1 = ((df5["Log Nmbr"] * 8) + 26)
    avg_vol = pd.DataFrame(Avg_vol1)
    df35 = df5[df5['Log Nmbr'].isin(avg_vol['Log Nmbr'])]
    df35['Avg Vol'] = (df35['dec7'] * 256) + (df35['dec8'])
    df36 = df35.drop(df35.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df37 = df36.reset_index()
    df38 = df37.drop(df37.columns[[0]], axis=1)
    df39 = pd.concat([df34, df38], axis=1)
    timestamp1 = ((df5["Log Nmbr"] * 8) + 25)
    timestamp = pd.DataFrame(timestamp1)
    df40 = df5[df5['Log Nmbr'].isin(timestamp['Log Nmbr'])]
    df40['timestamp'] = (df40['dec1'] * 16777216) + (df40['dec2'] * 65536) + (df40['dec3'] * 256) + (df40['dec4'])
    df41 = df40.drop(df40.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df42 = df41.reset_index()
    df43 = df42.drop(df42.columns[[0]], axis=1)
    df44 = pd.concat([df39, df43], axis=1)
    vcellH1 = ((df5["Log Nmbr"] * 8) + 27)
    vcellH = pd.DataFrame(vcellH1)
    df45 = df5[df5['Log Nmbr'].isin(vcellH['Log Nmbr'])]
    df45['V Cell H'] = (df45['dec1'] * 256) + (df45['dec2'])
    df46 = df45.drop(df45.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df47 = df46.reset_index()
    df48 = df47.drop(df47.columns[[0]], axis=1)
    df49 = pd.concat([df44, df48], axis=1)
    soc1 = ((df5["Log Nmbr"] * 8) + 27)
    soc = pd.DataFrame(soc1)
    df50 = df5[df5['Log Nmbr'].isin(soc['Log Nmbr'])]
    df50['SOC'] = (df50['dec5'])
    df51 = df50.drop(df50.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df52 = df51.reset_index()
    df53 = df52.drop(df52.columns[[0]], axis=1)
    df54 = pd.concat([df49, df53], axis=1)
    Avg_temp1 = ((df5["Log Nmbr"] * 8) + 27)
    Avg_temp = pd.DataFrame(Avg_temp1)
    df55 = df5[df5['Log Nmbr'].isin(Avg_temp['Log Nmbr'])]
    df55['Avg Temp'] = (df55['dec6'] * 256) + (df55['dec7'])
    df56 = df55.drop(df55.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df57 = df56.reset_index()
    df58 = df57.drop(df57.columns[[0]], axis=1)
    df59 = pd.concat([df54, df58], axis=1)
    V_cellL1 = ((df5["Log Nmbr"] * 8) + 27)
    V_cellL = pd.DataFrame(V_cellL1)
    df60 = df5[df5['Log Nmbr'].isin(V_cellL['Log Nmbr'])]
    df60['V Cell L'] = (df60['dec3'] * 256) + (df60['dec4'])
    df61 = df60.drop(df60.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df62 = df61.reset_index()
    df63 = df62.drop(df62.columns[[0]], axis=1)
    df64 = pd.concat([df59, df63], axis=1)
    SOH1 = ((df5["Log Nmbr"] * 8) + 29)
    SOH = pd.DataFrame(SOH1)
    df65 = df5[df5['Log Nmbr'].isin(SOH['Log Nmbr'])]
    df65['SOH'] = (df65['dec8'])
    df66 = df65.drop(df65.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df67 = df66.reset_index()
    df68 = df67.drop(df67.columns[[0]], axis=1)
    df69 = pd.concat([df64, df68], axis=1)
    max_current = ((df5["Log Nmbr"] * 8) + 30)
    max_cur = pd.DataFrame(max_current)
    df70 = df5[df5['Log Nmbr'].isin(max_cur['Log Nmbr'])]
    df70['Max Current Seen'] = (df70['dec1'] * 256) + (df70['dec2'])
    df71 = df70.drop(df70.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df72 = df71.reset_index()
    df73 = df72.drop(df72.columns[[0]], axis=1)
    df74 = pd.concat([df69, df73], axis=1)
    min_current = ((df5["Log Nmbr"] * 8) + 30)
    min_cur = pd.DataFrame(min_current)
    df75 = df5[df5['Log Nmbr'].isin(min_cur['Log Nmbr'])]
    df75['Min Current Seen'] = (df75['dec3'] * 256) + (df75['dec4'])
    df76 = df75.drop(df75.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df77 = df76.reset_index()
    df78 = df77.drop(df77.columns[[0]], axis=1)
    df79 = pd.concat([df74, df78], axis=1)
    H_Vcell1 = ((df5["Log Nmbr"] * 8) + 30)
    H_Vcell = pd.DataFrame(H_Vcell1)
    df80 = df5[df5['Log Nmbr'].isin(H_Vcell['Log Nmbr'])]
    df80['Highest VCell Seen'] = (df80['dec5'] * 256) + (df80['dec6'])
    df81 = df80.drop(df80.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df82 = df81.reset_index()
    df83 = df82.drop(df82.columns[[0]], axis=1)
    df84 = pd.concat([df79, df83], axis=1)
    L_Vcell1 = ((df5["Log Nmbr"] * 8) + 30)
    L_cell = pd.DataFrame(L_Vcell1)
    df85 = df5[df5['Log Nmbr'].isin(L_cell['Log Nmbr'])]
    df85['Lowest VCell Seen'] = (df85['dec7'] * 256) + (df85['dec8'])
    df86 = df85.drop(df85.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df87 = df86.reset_index()
    df88 = df87.drop(df87.columns[[0]], axis=1)
    df89 = pd.concat([df84, df88], axis=1)
    max_temp1 = ((df5["Log Nmbr"] * 8) + 31)
    max_temp = pd.DataFrame(max_temp1)
    df90 = df5[df5['Log Nmbr'].isin(max_temp['Log Nmbr'])]
    df90['Max Temp Seen'] = (df90['dec1'] * 256) + (df90['dec2'])
    df91 = df90.drop(df90.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df92 = df91.reset_index()
    df93 = df92.drop(df92.columns[[0]], axis=1)
    df94 = pd.concat([df89, df93], axis=1)
    min_temp1 = ((df5["Log Nmbr"] * 8) + 31)
    min_temp = pd.DataFrame(min_temp1)
    df95 = df5[df5['Log Nmbr'].isin(min_temp['Log Nmbr'])]
    df95['Min Temp Seen'] = (df95['dec3'] * 256) + (df95['dec4'])
    df96 = df95.drop(df95.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df97 = df96.reset_index()
    df98 = df97.drop(df97.columns[[0]], axis=1)
    df99 = pd.concat([df94, df98], axis=1)
    time1 = ((df5["Log Nmbr"] * 8) + 31)
    time = pd.DataFrame(time1)
    df100 = df5[df5['Log Nmbr'].isin(time['Log Nmbr'])]
    df100['Time Between Charges'] = (df100['dec5'] * 256) + (df100['dec6'])
    df101 = df100.drop(df100.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df102 = df101.reset_index()
    df103 = df102.drop(df102.columns[[0]], axis=1)
    df104 = pd.concat([df99, df103], axis=1)
    turn1 = ((df5["Log Nmbr"] * 8) + 32)
    turn = pd.DataFrame(turn1)
    df105 = df5[df5['Log Nmbr'].isin(turn['Log Nmbr'])]
    df105['Turn On Off Code'] = (df105['dec3'] * 256) + (df105['dec4'])
    df106 = df105.drop(df105.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df107 = df106.reset_index()
    df108 = df107.drop(df107.columns[[0]], axis=1)
    df109 = pd.concat([df104, df108], axis=1)
    lastchg1 = ((df5["Log Nmbr"] * 8) + 31)
    lastchg1F = pd.DataFrame(lastchg1)
    df110 = df5[df5['Log Nmbr'].isin(lastchg1F['Log Nmbr'])]
    df110['chg1'] = (df110['dec7'] * 16777216) + (df110['dec8'] * 65536)
    df111 = df110.drop(df110.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df112 = df111.reset_index()
    df113 = df112.drop(df112.columns[[0]], axis=1)
    lastchg2 = ((df5["Log Nmbr"] * 8) + 32)
    lastchg1G = pd.DataFrame(lastchg2)
    df114 = df5[df5['Log Nmbr'].isin(lastchg1G['Log Nmbr'])]
    df114['chg2'] = (df114['dec1'] * 256) + (df114['dec2'])
    df115 = df114.drop(df114.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df116 = df115.reset_index()
    df117 = df116.drop(df116.columns[[0]], axis=1)
    df117['Last Charge'] = (df113['chg1']) + (df117['chg2'])
    df118 = df117.drop(df117.columns[[0]], axis=1)
    df119 = pd.concat([df109, df118], axis=1)
    df120 = df119.assign(Capacity=None, Impedance=None)
    df121 = df120[
        ['Log Number', 'timestamp', 'Status', 'Error_Flag', 'Nbr Cycle', 'Nbr Reset', 'Current', 'Avg Vol', 'V Cell H',
         'V Cell L', 'SOC', 'Avg Temp', 'Impedance', 'Capacity', 'SOH', 'Max Current Seen', 'Min Current Seen',
         'Highest VCell Seen', 'Lowest VCell Seen', 'Max Temp Seen', 'Min Temp Seen', 'Time Between Charges',
         'Last Charge',
         'Turn On Off Code']]

    # with pd.ExcelWriter('C:\\Users\\Hamza Tufail\\Desktop\\sully\\EEPROMAnalyser.xlsx') as writer:
    # df4.to_excel(writer, sheet_name='EEPROM Decimal', index=False)
    # df109.to_excel(writer, sheet_name='Cyclic Data Raw', index=False)

    df = df121


    @st.experimental_memo
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')


    csv = convert_df(df)

    st.download_button(
        "Click to Download",
        csv,
        "Cyclic Data Raw.csv",
        "text/csv",
        key='download-csv'
    )

if '18FFFF81' in User_input:
    df2 = df199.drop(df199.columns[[0, 1, 2, 3, 4]], axis=1)
    df3 = (df199[df199.eq("18FFFF81").any(1)])
    df4 = df3.drop(df3.columns[[0, 1, 2, 3, 4]], axis=1)
    df4.columns = ['dec1', 'dec2', 'dec3', 'dec4', 'dec5', 'dec6', 'dec7', 'dec8']
    df5 = df4[['dec1', 'dec2', 'dec3', 'dec4', 'dec5', 'dec6', 'dec7', 'dec8']].applymap(lambda n: int(n, 16))
    df5['Log Nmbr'] = range(1, len(df5) + 1)
    status1 = ((df5["Log Nmbr"] * 8) + 25)
    status = pd.DataFrame(status1)
    df6 = status.rename(columns={'Log Nmbr': 'statuscalc'})
    df7 = pd.concat([df5[['dec5']], df6], axis=1)
    df8 = pd.concat([df5[['Log Nmbr']], df7], axis=1)
    df9 = df8.drop(df8.columns[[2]], axis=1)
    df10 = df9[df9['Log Nmbr'].isin(status['Log Nmbr'])]
    df11 = df10.drop(df10.columns[[0]], axis=1)
    df12 = df11.rename(columns={'dec5': 'Status'})
    df13 = df5[df5['Log Nmbr'].isin(status['Log Nmbr'])]
    df14 = df13['Error_Flag'] = (df13['dec6'] * 65536) + (df13['dec7'] * 256) + (df13['dec8'])
    df15 = df13.drop(df13.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df16 = pd.concat([df12, df15], axis=1)
    df16['Log Number'] = range(1, len(df16) + 1)
    current1 = ((df5["Log Nmbr"] * 8) + 26)
    current = pd.DataFrame(current1)
    df17 = df5[df5['Log Nmbr'].isin(current['Log Nmbr'])]
    df17['Current'] = (df17['dec5'] * 256) + (df17['dec6'])
    df18 = df17.drop(df17.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df19 = df16.reset_index()
    df20 = df19.drop(df19.columns[[0]], axis=1)
    df21 = df18.reset_index()
    df22 = df21.drop(df21.columns[[0]], axis=1)
    df23 = pd.concat([df20, df22], axis=1)
    df24 = df23[['Log Number', 'Status', 'Error_Flag', 'Current']]
    nbr_cycle1 = ((df5["Log Nmbr"] * 8) + 26)
    nbr_cycle = pd.DataFrame(nbr_cycle1)
    df25 = df5[df5['Log Nmbr'].isin(nbr_cycle['Log Nmbr'])]
    df25['Nbr Cycle'] = (df25['dec1'] * 256) + (df25['dec2'])
    df26 = df25.drop(df25.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df27 = df26.reset_index()
    df28 = df27.drop(df27.columns[[0]], axis=1)
    df29 = pd.concat([df24, df28], axis=1)
    nbr_reset1 = ((df5["Log Nmbr"] * 8) + 26)
    nbr_reset = pd.DataFrame(nbr_reset1)
    df30 = df5[df5['Log Nmbr'].isin(nbr_reset['Log Nmbr'])]
    df30['Nbr Reset'] = (df30['dec3'] * 256) + (df30['dec4'])
    df31 = df30.drop(df30.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df32 = df31.reset_index()
    df33 = df32.drop(df32.columns[[0]], axis=1)
    df34 = pd.concat([df29, df33], axis=1)
    Avg_vol1 = ((df5["Log Nmbr"] * 8) + 26)
    avg_vol = pd.DataFrame(Avg_vol1)
    df35 = df5[df5['Log Nmbr'].isin(avg_vol['Log Nmbr'])]
    df35['Avg Vol'] = (df35['dec7'] * 256) + (df35['dec8'])
    df36 = df35.drop(df35.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df37 = df36.reset_index()
    df38 = df37.drop(df37.columns[[0]], axis=1)
    df39 = pd.concat([df34, df38], axis=1)
    timestamp1 = ((df5["Log Nmbr"] * 8) + 25)
    timestamp = pd.DataFrame(timestamp1)
    df40 = df5[df5['Log Nmbr'].isin(timestamp['Log Nmbr'])]
    df40['timestamp'] = (df40['dec1'] * 16777216) + (df40['dec2'] * 65536) + (df40['dec3'] * 256) + (df40['dec4'])
    df41 = df40.drop(df40.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df42 = df41.reset_index()
    df43 = df42.drop(df42.columns[[0]], axis=1)
    df44 = pd.concat([df39, df43], axis=1)
    vcellH1 = ((df5["Log Nmbr"] * 8) + 27)
    vcellH = pd.DataFrame(vcellH1)
    df45 = df5[df5['Log Nmbr'].isin(vcellH['Log Nmbr'])]
    df45['V Cell H'] = (df45['dec1'] * 256) + (df45['dec2'])
    df46 = df45.drop(df45.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df47 = df46.reset_index()
    df48 = df47.drop(df47.columns[[0]], axis=1)
    df49 = pd.concat([df44, df48], axis=1)
    soc1 = ((df5["Log Nmbr"] * 8) + 27)
    soc = pd.DataFrame(soc1)
    df50 = df5[df5['Log Nmbr'].isin(soc['Log Nmbr'])]
    df50['SOC'] = (df50['dec5'])
    df51 = df50.drop(df50.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df52 = df51.reset_index()
    df53 = df52.drop(df52.columns[[0]], axis=1)
    df54 = pd.concat([df49, df53], axis=1)
    Avg_temp1 = ((df5["Log Nmbr"] * 8) + 27)
    Avg_temp = pd.DataFrame(Avg_temp1)
    df55 = df5[df5['Log Nmbr'].isin(Avg_temp['Log Nmbr'])]
    df55['Avg Temp'] = (df55['dec6'] * 256) + (df55['dec7'])
    df56 = df55.drop(df55.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df57 = df56.reset_index()
    df58 = df57.drop(df57.columns[[0]], axis=1)
    df59 = pd.concat([df54, df58], axis=1)
    V_cellL1 = ((df5["Log Nmbr"] * 8) + 27)
    V_cellL = pd.DataFrame(V_cellL1)
    df60 = df5[df5['Log Nmbr'].isin(V_cellL['Log Nmbr'])]
    df60['V Cell L'] = (df60['dec3'] * 256) + (df60['dec4'])
    df61 = df60.drop(df60.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df62 = df61.reset_index()
    df63 = df62.drop(df62.columns[[0]], axis=1)
    df64 = pd.concat([df59, df63], axis=1)
    SOH1 = ((df5["Log Nmbr"] * 8) + 29)
    SOH = pd.DataFrame(SOH1)
    df65 = df5[df5['Log Nmbr'].isin(SOH['Log Nmbr'])]
    df65['SOH'] = (df65['dec8'])
    df66 = df65.drop(df65.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df67 = df66.reset_index()
    df68 = df67.drop(df67.columns[[0]], axis=1)
    df69 = pd.concat([df64, df68], axis=1)
    max_current = ((df5["Log Nmbr"] * 8) + 30)
    max_cur = pd.DataFrame(max_current)
    df70 = df5[df5['Log Nmbr'].isin(max_cur['Log Nmbr'])]
    df70['Max Current Seen'] = (df70['dec1'] * 256) + (df70['dec2'])
    df71 = df70.drop(df70.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df72 = df71.reset_index()
    df73 = df72.drop(df72.columns[[0]], axis=1)
    df74 = pd.concat([df69, df73], axis=1)
    min_current = ((df5["Log Nmbr"] * 8) + 30)
    min_cur = pd.DataFrame(min_current)
    df75 = df5[df5['Log Nmbr'].isin(min_cur['Log Nmbr'])]
    df75['Min Current Seen'] = (df75['dec3'] * 256) + (df75['dec4'])
    df76 = df75.drop(df75.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df77 = df76.reset_index()
    df78 = df77.drop(df77.columns[[0]], axis=1)
    df79 = pd.concat([df74, df78], axis=1)
    H_Vcell1 = ((df5["Log Nmbr"] * 8) + 30)
    H_Vcell = pd.DataFrame(H_Vcell1)
    df80 = df5[df5['Log Nmbr'].isin(H_Vcell['Log Nmbr'])]
    df80['Highest VCell Seen'] = (df80['dec5'] * 256) + (df80['dec6'])
    df81 = df80.drop(df80.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df82 = df81.reset_index()
    df83 = df82.drop(df82.columns[[0]], axis=1)
    df84 = pd.concat([df79, df83], axis=1)
    L_Vcell1 = ((df5["Log Nmbr"] * 8) + 30)
    L_cell = pd.DataFrame(L_Vcell1)
    df85 = df5[df5['Log Nmbr'].isin(L_cell['Log Nmbr'])]
    df85['Lowest VCell Seen'] = (df85['dec7'] * 256) + (df85['dec8'])
    df86 = df85.drop(df85.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df87 = df86.reset_index()
    df88 = df87.drop(df87.columns[[0]], axis=1)
    df89 = pd.concat([df84, df88], axis=1)
    max_temp1 = ((df5["Log Nmbr"] * 8) + 31)
    max_temp = pd.DataFrame(max_temp1)
    df90 = df5[df5['Log Nmbr'].isin(max_temp['Log Nmbr'])]
    df90['Max Temp Seen'] = (df90['dec1'] * 256) + (df90['dec2'])
    df91 = df90.drop(df90.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df92 = df91.reset_index()
    df93 = df92.drop(df92.columns[[0]], axis=1)
    df94 = pd.concat([df89, df93], axis=1)
    min_temp1 = ((df5["Log Nmbr"] * 8) + 31)
    min_temp = pd.DataFrame(min_temp1)
    df95 = df5[df5['Log Nmbr'].isin(min_temp['Log Nmbr'])]
    df95['Min Temp Seen'] = (df95['dec3'] * 256) + (df95['dec4'])
    df96 = df95.drop(df95.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df97 = df96.reset_index()
    df98 = df97.drop(df97.columns[[0]], axis=1)
    df99 = pd.concat([df94, df98], axis=1)
    time1 = ((df5["Log Nmbr"] * 8) + 31)
    time = pd.DataFrame(time1)
    df100 = df5[df5['Log Nmbr'].isin(time['Log Nmbr'])]
    df100['Time Between Charges'] = (df100['dec5'] * 256) + (df100['dec6'])
    df101 = df100.drop(df100.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df102 = df101.reset_index()
    df103 = df102.drop(df102.columns[[0]], axis=1)
    df104 = pd.concat([df99, df103], axis=1)
    turn1 = ((df5["Log Nmbr"] * 8) + 32)
    turn = pd.DataFrame(turn1)
    df105 = df5[df5['Log Nmbr'].isin(turn['Log Nmbr'])]
    df105['Turn On Off Code'] = (df105['dec3'] * 256) + (df105['dec4'])
    df106 = df105.drop(df105.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df107 = df106.reset_index()
    df108 = df107.drop(df107.columns[[0]], axis=1)
    df109 = pd.concat([df104, df108], axis=1)
    lastchg1 = ((df5["Log Nmbr"] * 8) + 31)
    lastchg1F = pd.DataFrame(lastchg1)
    df110 = df5[df5['Log Nmbr'].isin(lastchg1F['Log Nmbr'])]
    df110['chg1'] = (df110['dec7'] * 16777216) + (df110['dec8'] * 65536)
    df111 = df110.drop(df110.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df112 = df111.reset_index()
    df113 = df112.drop(df112.columns[[0]], axis=1)
    lastchg2 = ((df5["Log Nmbr"] * 8) + 32)
    lastchg1G = pd.DataFrame(lastchg2)
    df114 = df5[df5['Log Nmbr'].isin(lastchg1G['Log Nmbr'])]
    df114['chg2'] = (df114['dec1'] * 256) + (df114['dec2'])
    df115 = df114.drop(df114.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df116 = df115.reset_index()
    df117 = df116.drop(df116.columns[[0]], axis=1)
    df117['Last Charge'] = (df113['chg1']) + (df117['chg2'])
    df118 = df117.drop(df117.columns[[0]], axis=1)
    df119 = pd.concat([df109, df118], axis=1)
    df120 = df119.assign(Capacity=None, Impedance=None)
    df121 = df120[
        ['Log Number', 'timestamp', 'Status', 'Error_Flag', 'Nbr Cycle', 'Nbr Reset', 'Current', 'Avg Vol', 'V Cell H',
         'V Cell L', 'SOC', 'Avg Temp', 'Impedance', 'Capacity', 'SOH', 'Max Current Seen', 'Min Current Seen',
         'Highest VCell Seen', 'Lowest VCell Seen', 'Max Temp Seen', 'Min Temp Seen', 'Time Between Charges',
         'Last Charge',
         'Turn On Off Code']]

    # with pd.ExcelWriter('C:\\Users\\Hamza Tufail\\Desktop\\sully\\EEPROMAnalyser.xlsx') as writer:
    # df4.to_excel(writer, sheet_name='EEPROM Decimal', index=False)
    # df109.to_excel(writer, sheet_name='Cyclic Data Raw', index=False)

    df = df121


    @st.experimental_memo
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')


    csv = convert_df(df)

    st.download_button(
        "Click to Download",
        csv,
        "Cyclic Data Raw.csv",
        "text/csv",
        key='download-csv'
    )

if '18FFFF82' in User_input:
    df2 = df199.drop(df199.columns[[0, 1, 2, 3, 4]], axis=1)
    df3 = (df199[df199.eq("18FFFF82").any(1)])
    df4 = df3.drop(df3.columns[[0, 1, 2, 3, 4]], axis=1)
    df4.columns = ['dec1', 'dec2', 'dec3', 'dec4', 'dec5', 'dec6', 'dec7', 'dec8']
    df5 = df4[['dec1', 'dec2', 'dec3', 'dec4', 'dec5', 'dec6', 'dec7', 'dec8']].applymap(lambda n: int(n, 16))
    df5['Log Nmbr'] = range(1, len(df5) + 1)
    status1 = ((df5["Log Nmbr"] * 8) + 25)
    status = pd.DataFrame(status1)
    df6 = status.rename(columns={'Log Nmbr': 'statuscalc'})
    df7 = pd.concat([df5[['dec5']], df6], axis=1)
    df8 = pd.concat([df5[['Log Nmbr']], df7], axis=1)
    df9 = df8.drop(df8.columns[[2]], axis=1)
    df10 = df9[df9['Log Nmbr'].isin(status['Log Nmbr'])]
    df11 = df10.drop(df10.columns[[0]], axis=1)
    df12 = df11.rename(columns={'dec5': 'Status'})
    df13 = df5[df5['Log Nmbr'].isin(status['Log Nmbr'])]
    df14 = df13['Error_Flag'] = (df13['dec6'] * 65536) + (df13['dec7'] * 256) + (df13['dec8'])
    df15 = df13.drop(df13.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df16 = pd.concat([df12, df15], axis=1)
    df16['Log Number'] = range(1, len(df16) + 1)
    current1 = ((df5["Log Nmbr"] * 8) + 26)
    current = pd.DataFrame(current1)
    df17 = df5[df5['Log Nmbr'].isin(current['Log Nmbr'])]
    df17['Current'] = (df17['dec5'] * 256) + (df17['dec6'])
    df18 = df17.drop(df17.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df19 = df16.reset_index()
    df20 = df19.drop(df19.columns[[0]], axis=1)
    df21 = df18.reset_index()
    df22 = df21.drop(df21.columns[[0]], axis=1)
    df23 = pd.concat([df20, df22], axis=1)
    df24 = df23[['Log Number', 'Status', 'Error_Flag', 'Current']]
    nbr_cycle1 = ((df5["Log Nmbr"] * 8) + 26)
    nbr_cycle = pd.DataFrame(nbr_cycle1)
    df25 = df5[df5['Log Nmbr'].isin(nbr_cycle['Log Nmbr'])]
    df25['Nbr Cycle'] = (df25['dec1'] * 256) + (df25['dec2'])
    df26 = df25.drop(df25.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df27 = df26.reset_index()
    df28 = df27.drop(df27.columns[[0]], axis=1)
    df29 = pd.concat([df24, df28], axis=1)
    nbr_reset1 = ((df5["Log Nmbr"] * 8) + 26)
    nbr_reset = pd.DataFrame(nbr_reset1)
    df30 = df5[df5['Log Nmbr'].isin(nbr_reset['Log Nmbr'])]
    df30['Nbr Reset'] = (df30['dec3'] * 256) + (df30['dec4'])
    df31 = df30.drop(df30.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df32 = df31.reset_index()
    df33 = df32.drop(df32.columns[[0]], axis=1)
    df34 = pd.concat([df29, df33], axis=1)
    Avg_vol1 = ((df5["Log Nmbr"] * 8) + 26)
    avg_vol = pd.DataFrame(Avg_vol1)
    df35 = df5[df5['Log Nmbr'].isin(avg_vol['Log Nmbr'])]
    df35['Avg Vol'] = (df35['dec7'] * 256) + (df35['dec8'])
    df36 = df35.drop(df35.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df37 = df36.reset_index()
    df38 = df37.drop(df37.columns[[0]], axis=1)
    df39 = pd.concat([df34, df38], axis=1)
    timestamp1 = ((df5["Log Nmbr"] * 8) + 25)
    timestamp = pd.DataFrame(timestamp1)
    df40 = df5[df5['Log Nmbr'].isin(timestamp['Log Nmbr'])]
    df40['timestamp'] = (df40['dec1'] * 16777216) + (df40['dec2'] * 65536) + (df40['dec3'] * 256) + (df40['dec4'])
    df41 = df40.drop(df40.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df42 = df41.reset_index()
    df43 = df42.drop(df42.columns[[0]], axis=1)
    df44 = pd.concat([df39, df43], axis=1)
    vcellH1 = ((df5["Log Nmbr"] * 8) + 27)
    vcellH = pd.DataFrame(vcellH1)
    df45 = df5[df5['Log Nmbr'].isin(vcellH['Log Nmbr'])]
    df45['V Cell H'] = (df45['dec1'] * 256) + (df45['dec2'])
    df46 = df45.drop(df45.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df47 = df46.reset_index()
    df48 = df47.drop(df47.columns[[0]], axis=1)
    df49 = pd.concat([df44, df48], axis=1)
    soc1 = ((df5["Log Nmbr"] * 8) + 27)
    soc = pd.DataFrame(soc1)
    df50 = df5[df5['Log Nmbr'].isin(soc['Log Nmbr'])]
    df50['SOC'] = (df50['dec5'])
    df51 = df50.drop(df50.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df52 = df51.reset_index()
    df53 = df52.drop(df52.columns[[0]], axis=1)
    df54 = pd.concat([df49, df53], axis=1)
    Avg_temp1 = ((df5["Log Nmbr"] * 8) + 27)
    Avg_temp = pd.DataFrame(Avg_temp1)
    df55 = df5[df5['Log Nmbr'].isin(Avg_temp['Log Nmbr'])]
    df55['Avg Temp'] = (df55['dec6'] * 256) + (df55['dec7'])
    df56 = df55.drop(df55.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df57 = df56.reset_index()
    df58 = df57.drop(df57.columns[[0]], axis=1)
    df59 = pd.concat([df54, df58], axis=1)
    V_cellL1 = ((df5["Log Nmbr"] * 8) + 27)
    V_cellL = pd.DataFrame(V_cellL1)
    df60 = df5[df5['Log Nmbr'].isin(V_cellL['Log Nmbr'])]
    df60['V Cell L'] = (df60['dec3'] * 256) + (df60['dec4'])
    df61 = df60.drop(df60.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df62 = df61.reset_index()
    df63 = df62.drop(df62.columns[[0]], axis=1)
    df64 = pd.concat([df59, df63], axis=1)
    SOH1 = ((df5["Log Nmbr"] * 8) + 29)
    SOH = pd.DataFrame(SOH1)
    df65 = df5[df5['Log Nmbr'].isin(SOH['Log Nmbr'])]
    df65['SOH'] = (df65['dec8'])
    df66 = df65.drop(df65.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df67 = df66.reset_index()
    df68 = df67.drop(df67.columns[[0]], axis=1)
    df69 = pd.concat([df64, df68], axis=1)
    max_current = ((df5["Log Nmbr"] * 8) + 30)
    max_cur = pd.DataFrame(max_current)
    df70 = df5[df5['Log Nmbr'].isin(max_cur['Log Nmbr'])]
    df70['Max Current Seen'] = (df70['dec1'] * 256) + (df70['dec2'])
    df71 = df70.drop(df70.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df72 = df71.reset_index()
    df73 = df72.drop(df72.columns[[0]], axis=1)
    df74 = pd.concat([df69, df73], axis=1)
    min_current = ((df5["Log Nmbr"] * 8) + 30)
    min_cur = pd.DataFrame(min_current)
    df75 = df5[df5['Log Nmbr'].isin(min_cur['Log Nmbr'])]
    df75['Min Current Seen'] = (df75['dec3'] * 256) + (df75['dec4'])
    df76 = df75.drop(df75.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df77 = df76.reset_index()
    df78 = df77.drop(df77.columns[[0]], axis=1)
    df79 = pd.concat([df74, df78], axis=1)
    H_Vcell1 = ((df5["Log Nmbr"] * 8) + 30)
    H_Vcell = pd.DataFrame(H_Vcell1)
    df80 = df5[df5['Log Nmbr'].isin(H_Vcell['Log Nmbr'])]
    df80['Highest VCell Seen'] = (df80['dec5'] * 256) + (df80['dec6'])
    df81 = df80.drop(df80.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df82 = df81.reset_index()
    df83 = df82.drop(df82.columns[[0]], axis=1)
    df84 = pd.concat([df79, df83], axis=1)
    L_Vcell1 = ((df5["Log Nmbr"] * 8) + 30)
    L_cell = pd.DataFrame(L_Vcell1)
    df85 = df5[df5['Log Nmbr'].isin(L_cell['Log Nmbr'])]
    df85['Lowest VCell Seen'] = (df85['dec7'] * 256) + (df85['dec8'])
    df86 = df85.drop(df85.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df87 = df86.reset_index()
    df88 = df87.drop(df87.columns[[0]], axis=1)
    df89 = pd.concat([df84, df88], axis=1)
    max_temp1 = ((df5["Log Nmbr"] * 8) + 31)
    max_temp = pd.DataFrame(max_temp1)
    df90 = df5[df5['Log Nmbr'].isin(max_temp['Log Nmbr'])]
    df90['Max Temp Seen'] = (df90['dec1'] * 256) + (df90['dec2'])
    df91 = df90.drop(df90.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df92 = df91.reset_index()
    df93 = df92.drop(df92.columns[[0]], axis=1)
    df94 = pd.concat([df89, df93], axis=1)
    min_temp1 = ((df5["Log Nmbr"] * 8) + 31)
    min_temp = pd.DataFrame(min_temp1)
    df95 = df5[df5['Log Nmbr'].isin(min_temp['Log Nmbr'])]
    df95['Min Temp Seen'] = (df95['dec3'] * 256) + (df95['dec4'])
    df96 = df95.drop(df95.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df97 = df96.reset_index()
    df98 = df97.drop(df97.columns[[0]], axis=1)
    df99 = pd.concat([df94, df98], axis=1)
    time1 = ((df5["Log Nmbr"] * 8) + 31)
    time = pd.DataFrame(time1)
    df100 = df5[df5['Log Nmbr'].isin(time['Log Nmbr'])]
    df100['Time Between Charges'] = (df100['dec5'] * 256) + (df100['dec6'])
    df101 = df100.drop(df100.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df102 = df101.reset_index()
    df103 = df102.drop(df102.columns[[0]], axis=1)
    df104 = pd.concat([df99, df103], axis=1)
    turn1 = ((df5["Log Nmbr"] * 8) + 32)
    turn = pd.DataFrame(turn1)
    df105 = df5[df5['Log Nmbr'].isin(turn['Log Nmbr'])]
    df105['Turn On Off Code'] = (df105['dec3'] * 256) + (df105['dec4'])
    df106 = df105.drop(df105.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df107 = df106.reset_index()
    df108 = df107.drop(df107.columns[[0]], axis=1)
    df109 = pd.concat([df104, df108], axis=1)
    lastchg1 = ((df5["Log Nmbr"] * 8) + 31)
    lastchg1F = pd.DataFrame(lastchg1)
    df110 = df5[df5['Log Nmbr'].isin(lastchg1F['Log Nmbr'])]
    df110['chg1'] = (df110['dec7'] * 16777216) + (df110['dec8'] * 65536)
    df111 = df110.drop(df110.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df112 = df111.reset_index()
    df113 = df112.drop(df112.columns[[0]], axis=1)
    lastchg2 = ((df5["Log Nmbr"] * 8) + 32)
    lastchg1G = pd.DataFrame(lastchg2)
    df114 = df5[df5['Log Nmbr'].isin(lastchg1G['Log Nmbr'])]
    df114['chg2'] = (df114['dec1'] * 256) + (df114['dec2'])
    df115 = df114.drop(df114.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8]], axis=1)
    df116 = df115.reset_index()
    df117 = df116.drop(df116.columns[[0]], axis=1)
    df117['Last Charge'] = (df113['chg1']) + (df117['chg2'])
    df118 = df117.drop(df117.columns[[0]], axis=1)
    df119 = pd.concat([df109, df118], axis=1)
    df120 = df119.assign(Capacity=None, Impedance=None)
    df121 = df120[
        ['Log Number', 'timestamp', 'Status', 'Error_Flag', 'Nbr Cycle', 'Nbr Reset', 'Current', 'Avg Vol', 'V Cell H',
         'V Cell L', 'SOC', 'Avg Temp', 'Impedance', 'Capacity', 'SOH', 'Max Current Seen', 'Min Current Seen',
         'Highest VCell Seen', 'Lowest VCell Seen', 'Max Temp Seen', 'Min Temp Seen', 'Time Between Charges',
         'Last Charge',
         'Turn On Off Code']]

    # with pd.ExcelWriter('C:\\Users\\Hamza Tufail\\Desktop\\sully\\EEPROMAnalyser.xlsx') as writer:
    # df4.to_excel(writer, sheet_name='EEPROM Decimal', index=False)
    # df109.to_excel(writer, sheet_name='Cyclic Data Raw', index=False)

    df = df121


    @st.experimental_memo
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')


    csv = convert_df(df)

    st.download_button(
        "Click to Download",
        csv,
        "Cyclic Data Raw.csv",
        "text/csv",
        key='download-csv'
    )

    # ignore warning
    # initial file upload
