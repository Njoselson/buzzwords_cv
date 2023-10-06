import streamlit as st
from linkedin_api import Linkedin

DOWNLOAD = False

st.write("First Log in to read from api")
api = Linkedin("nathaniel.joselson@gmail.com", "ilovemaja1000")
profile = api.get_profile("nathaniel-joselson-301687132")

st.write("Make data caching on some basic funcs")
api.get_job = st.cache_data(api.get_job)
api.search_jobs = st.cache_data(api.search_jobs)


if DOWNLOAD:
    st.write("Get Data from Linkedin")

    st.write("Then get a specific job by id")
    job = api.get_job("3584509761")
    st.write("Get Job description text")
    st.write(job.get("description").get("text"))

st.write("Now lets look at a list of jobs")
job_list = api.search_jobs(
    keywords=["machine learning"], location_name="New York, New York", limit=10
)
st.write(job_list)
