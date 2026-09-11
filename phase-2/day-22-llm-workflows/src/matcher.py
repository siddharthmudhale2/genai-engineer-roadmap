from src.models import Candidate, Job, JobMatch


class JobMatcher:
    def match(
        self,
        candidate: Candidate,
        job: Job,
    ) -> JobMatch:
        candidate_skills = {
            skill.lower()
            for skill in candidate.skills
        }

        required_skills = {
            skill.lower()
            for skill in job.required_skills
        }

        matching = candidate_skills & required_skills
        missing = required_skills - candidate_skills

        if required_skills:
            score = int(
                len(matching) / len(required_skills) * 100
            )
        else:
            score = 100

        return JobMatch(
            match_score=score,
            matching_skills=sorted(matching),
            missing_skills=sorted(missing),
        )