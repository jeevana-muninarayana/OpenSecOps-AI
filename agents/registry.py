from agents.example_agent import ExampleAgent
from agents.enrichment_agent import EnrichmentAgent
from agents.threat_scoring_agent import ThreatScoringAgent
from agents.live_feed_agent import LiveFeedAgent
from agents.log_correlation_agent import LogCorrelationAgent

AGENT_REGISTRY = {
    "example_agent": ExampleAgent(),
    "enrichment_agent": EnrichmentAgent(),
    "threat_scoring_agent": ThreatScoringAgent(),
    "live_feed_agent": LiveFeedAgent(),
    "log_correlation_agent": LogCorrelationAgent()
}
