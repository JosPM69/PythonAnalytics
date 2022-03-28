import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport


df = pd.read_csv("data/Data_limpia.csv", na_values=['='])




profile = ProfileReport(df, title="Salario Data", dataset={
        "description": "This profiling report was generated for Analytics",
        "copyright_holder": "Análisis por Josué Pérez",
        "copyright_year": "2022"},
    variables={
        "descriptions": {
            "company": "Nombres de las compañías",
            "totalyearlycompensation": "Compensación total anual",
            "yearsofexperience": "Años de experiencia",
            "yearsatcompany": "Años en la compañía",
            "basesalary": "Salario base",
            "stockgrantvalue": "Concesión de acciones",
            "bonus": "Bonus",
            "gender": "Género",
            "Race": "Raza",
            "Education": "Nivel de educación"
        }
    }
)


st.title("Reporte de Pandas profiling en Streamlit")
st.write(df)
st_profile_report(profile)