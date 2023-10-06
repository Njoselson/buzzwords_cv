import linkedin_api as linkedin 
import logging



class BuzzWordGetter:
    def __init__(self):
        logging.info("Logging in to linkedin api")
        self.login = ("nathaniel.joselson@gmail.com", "ilovemaja1000")
        try:
            self.linkedin_api = linkedin.Linkedin(*self.login)
        except linkedin.cookie_repository.LinkedinSessionExpired:
            self.linkedin_api = linkedin.Linkedin(*self.login,refresh_cookies=True)

        # self.linkedin_profile = self.linkedin_api.get_profile(
        #     "nathaniel-joselson-301687132"
        # )

    def get_jobs(self, topic, number):
        logging.info("Getting a list of jobs")
        jobs_list = self.linkedin_api.search_jobs(
            keywords=[topic], location_name="San Francisco California", limit=number
        )
        logging.debug(f'{jobs_list=}')
        self.jobs_list = [job["dashEntityUrn"].split(':')[-1] for job in jobs_list]

        logging.info(
            "gathered the following jobs"
            + f"{self.jobs_list[:2]}"
        )

    def get_job_text(self):
        self.job_text = ""
        for job_id in self.jobs_list:
            job = self.linkedin_api.get_job(job_id)
            self.job_text += job.get("description").get("text")

        logging.info(f"example job text: {self.job_text[:100]}")


       
