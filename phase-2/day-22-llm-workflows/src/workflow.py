from src.extractor import CandidateExtractor
from src.matcher import JobMatcher
from src.models import Job, Recommendation
from src.recommender import RecommendationGenerator


class JobApplicationWorkflow:
    def __init__(
        self,
        extractor: CandidateExtractor,
        matcher: JobMatcher,
        recommender: RecommendationGenerator,
    ):
        self.extractor = extractor
        self.matcher = matcher
        self.recommender = recommender

    def run(
        self,
        candidate_text: str,
        job: Job,
    ) -> Recommendation:
        candidate = self.extractor.extract(
            candidate_text
        )

        match = self.matcher.match(
            candidate,
            job,
        )

        recommendation = self.recommender.generate(
            match
        )

        return recommendation