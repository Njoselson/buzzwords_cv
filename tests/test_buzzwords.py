import pytest

from buzzwordscv.buzzwords import BuzzWordGetter


def test_gets_a_list_of_jobs_with_a_topic():
    topic = "Machine Learning"
    n_jobs = 2 

    buzzwordscv = BuzzWordGetter()
    buzzwordscv.get_jobs(topic=topic, number=n_jobs)
    assert len(buzzwordscv.jobs_list) == n_jobs

    for job in buzzwordscv.jobs_list:
        assert str(job).isnumeric()

def test_gets_text_for_jobs():
    topic = "Machine Learning"
    n_jobs = 2 

    buzzwordscv = BuzzWordGetter()
    buzzwordscv.get_jobs(topic=topic, number=n_jobs)
    buzzwordscv.get_job_text()
    assert len(buzzwordscv.job_text) > 0
    assert "and" in buzzwordscv.job_text

def test_counts_text_in_a_dict():
    pass

