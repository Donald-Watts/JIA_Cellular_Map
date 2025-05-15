"""
Biofield Synchronizer for JIA Cellular AI Mapping

This module implements the coordination system for multiple AI agents, ensuring
synchronized cognitive processing and field resonance across the simulation.
"""

import yaml
import json
from typing import Dict, List, Optional, Union
from dataclasses import dataclass
from datetime import datetime
import logging
from pathlib import Path

@dataclass
class AgentState:
    """Represents the current state of an AI agent."""
    name: str
    role: str
    weight: float
    last_update: datetime
    resonance_score: float
    harmonics: Dict[str, float]

@dataclass
class FieldState:
    """Represents the current state of a biofield."""
    field_id: str
    agents: List[AgentState]
    resonance_pattern: Dict[str, float]
    harmonics_score: float
    last_sync: datetime

class BiofieldSynchronizer:
    """Coordinates multiple AI agents in a synchronized cognitive system."""
    
    def __init__(self, config_path: str = "config/defaults.yaml"):
        """Initialize the synchronizer with configuration."""
        self.config = self._load_config(config_path)
        self.fields: Dict[str, FieldState] = {}
        self._setup_logging()
        
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML file."""
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def _setup_logging(self):
        """Configure logging for the synchronizer."""
        log_config = self.config["logging"]
        logging.basicConfig(
            level=getattr(logging, log_config["level"]),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            filename=log_config["file"],
            filemode='a'
        )
        self.logger = logging.getLogger("BiofieldSynchronizer")
    
    def create_field(self, field_id: str, agents: List[Dict[str, Union[str, float]]]) -> FieldState:
        """Create a new biofield with specified agents."""
        agent_states = [
            AgentState(
                name=agent["name"],
                role=agent["role"],
                weight=agent["weight"],
                last_update=datetime.now(),
                resonance_score=0.0,
                harmonics={}
            )
            for agent in agents
        ]
        
        field = FieldState(
            field_id=field_id,
            agents=agent_states,
            resonance_pattern={},
            harmonics_score=0.0,
            last_sync=datetime.now()
        )
        
        self.fields[field_id] = field
        self.logger.info(f"Created new field: {field_id}")
        return field
    
    def update_agent_state(self, field_id: str, agent_name: str, 
                          resonance_score: float, harmonics: Dict[str, float]) -> None:
        """Update the state of an agent within a field."""
        if field_id not in self.fields:
            raise ValueError(f"Field {field_id} does not exist")
            
        field = self.fields[field_id]
        for agent in field.agents:
            if agent.name == agent_name:
                agent.resonance_score = resonance_score
                agent.harmonics = harmonics
                agent.last_update = datetime.now()
                self.logger.info(f"Updated agent {agent_name} in field {field_id}")
                return
                
        raise ValueError(f"Agent {agent_name} not found in field {field_id}")
    
    def calculate_field_resonance(self, field_id: str) -> Dict[str, float]:
        """Calculate resonance patterns for a field based on agent states."""
        if field_id not in self.fields:
            raise ValueError(f"Field {field_id} does not exist")
            
        field = self.fields[field_id]
        resonance_pattern = {}
        
        # Calculate base resonance from agent states
        for agent in field.agents:
            for harmonic, value in agent.harmonics.items():
                resonance_pattern[harmonic] = resonance_pattern.get(harmonic, 0.0) + value * agent.weight
        
        # Apply resonance parameters from config
        resonance_config = self.config["resonance"]
        for harmonic in resonance_pattern:
            resonance_pattern[harmonic] *= resonance_config["coupling_strength"]
            resonance_pattern[harmonic] *= (1 - resonance_config["decay_rate"])
        
        field.resonance_pattern = resonance_pattern
        field.last_sync = datetime.now()
        
        self.logger.info(f"Calculated resonance for field {field_id}")
        return resonance_pattern
    
    def get_field_harmonics(self, field_id: str) -> float:
        """Calculate overall harmonics score for a field."""
        if field_id not in self.fields:
            raise ValueError(f"Field {field_id} does not exist")
            
        field = self.fields[field_id]
        harmonics_score = sum(field.resonance_pattern.values()) * self.config["resonance"]["harmonic_scaling"]
        field.harmonics_score = harmonics_score
        
        return harmonics_score
    
    def synchronize_field(self, field_id: str) -> Dict[str, Union[float, Dict[str, float]]]:
        """Synchronize all agents in a field and return updated state."""
        if field_id not in self.fields:
            raise ValueError(f"Field {field_id} does not exist")
            
        # Calculate new resonance pattern
        resonance_pattern = self.calculate_field_resonance(field_id)
        
        # Calculate overall harmonics
        harmonics_score = self.get_field_harmonics(field_id)
        
        # Update field state
        field = self.fields[field_id]
        field.last_sync = datetime.now()
        
        return {
            "field_id": field_id,
            "harmonics_score": harmonics_score,
            "resonance_pattern": resonance_pattern,
            "last_sync": field.last_sync.isoformat()
        }
    
    def save_field_state(self, field_id: str, output_path: str) -> None:
        """Save the current state of a field to a JSON file."""
        if field_id not in self.fields:
            raise ValueError(f"Field {field_id} does not exist")
            
        field = self.fields[field_id]
        state = {
            "field_id": field.field_id,
            "last_sync": field.last_sync.isoformat(),
            "harmonics_score": field.harmonics_score,
            "resonance_pattern": field.resonance_pattern,
            "agents": [
                {
                    "name": agent.name,
                    "role": agent.role,
                    "weight": agent.weight,
                    "last_update": agent.last_update.isoformat(),
                    "resonance_score": agent.resonance_score,
                    "harmonics": agent.harmonics
                }
                for agent in field.agents
            ]
        }
        
        with open(output_path, 'w') as f:
            json.dump(state, f, indent=2)
        
        self.logger.info(f"Saved field state to {output_path}")

def main():
    """Main entry point for biofield synchronization."""
    synchronizer = BiofieldSynchronizer()
    
    # Create initial field with primary agents
    field_id = "primary_field"
    agents = [
        {"name": "claude", "role": "nucleus", "weight": 0.4},
        {"name": "gpt", "role": "cytoplasm", "weight": 0.3},
        {"name": "gemini", "role": "membrane", "weight": 0.3}
    ]
    
    field = synchronizer.create_field(field_id, agents)
    
    # Update agent states
    synchronizer.update_agent_state(
        field_id, "claude",
        resonance_score=0.8,
        harmonics={"base": 0.9, "harmonic1": 0.7}
    )
    
    # Synchronize field
    state = synchronizer.synchronize_field(field_id)
    
    # Save state
    synchronizer.save_field_state(field_id, "field_state.json")

if __name__ == "__main__":
    main() 