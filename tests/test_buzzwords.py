import pytest

from buzzz.buzzwords import BuzzWordGetter


def test_gets_a_list_of_jobs_with_a_topic():
    topic = "Machine Learning"
    n_jobs = 2 

    buzzz = BuzzWordGetter()
    buzzz.get_jobs(topic=topic, number=n_jobs)
    assert len(buzzz.jobs_list) == n_jobs

    for job in buzzz.jobs_list:
        assert str(job).isnumeric()

def test_gets_text_for_jobs():
    topic = "Machine Learning"
    n_jobs = 2 

    buzzz = BuzzWordGetter()
    buzzz.get_jobs(topic=topic, number=n_jobs)
    buzzz.get_job_text()
    assert len(buzzz.job_text) > 0
    assert "and" in buzzz.job_text

def test_counts_text_in_a_dict():
    pass

