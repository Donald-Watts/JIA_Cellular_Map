#!/usr/bin/env python3
import re, sys, pathlib, textwrap
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass
from enum import Enum
import yaml
import os
from datetime import datetime

class CellType(Enum):
    IMMUNE = "immune"
    TISSUE = "tissue"
    FLUID = "fluid"
    SIGNAL = "signal"
    INTERVENTION = "intervention"

class AIAgent(Enum):
    CLAUDE = "claude"
    GPT = "gpt"
    GEMINI = "gemini"
    BIOBERT = "biobert"
    BART = "bart"

@dataclass
class WeightConfig:
    """Configuration for weight calculations."""
    base_weight: float
    direction_weight: float
    interaction_weight: float
    state_weight: float
    resonance_weight: float

@dataclass
class CellularWeight:
    """Represents the weight of a cellular component."""
    component_weight: float
    ai_direction_weight: float
    interaction_weight: float
    state_weight: float
    resonance_score: float
    field_harmonics: float

class WeightSystem:
    """Main weight system implementation."""
    
    def __init__(self, config_path: str = "config/defaults.yaml"):
        """Initialize the weight system with configuration."""
        self.config = self._load_config(config_path)
        self.weight_config = WeightConfig(**self.config["weight_system"])
        
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML file."""
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def calculate_cellular_weight(self, 
                                component_type: str,
                                state: Dict[str, float],
                                interactions: List[Dict[str, float]]) -> CellularWeight:
        """Calculate weights for a cellular component."""
        # Base component weight
        component_weight = self.weight_config.base_weight
        
        # AI direction weight based on agent roles
        ai_direction_weight = self._calculate_ai_direction_weight(state)
        
        # Interaction weight based on cellular interactions
        interaction_weight = self._calculate_interaction_weight(interactions)
        
        # State weight based on current cellular state
        state_weight = self._calculate_state_weight(state)
        
        # Resonance and harmonics calculations
        resonance_score = self._calculate_resonance_score(state, interactions)
        field_harmonics = self._calculate_field_harmonics(state)
        
        return CellularWeight(
            component_weight=component_weight,
            ai_direction_weight=ai_direction_weight,
            interaction_weight=interaction_weight,
            state_weight=state_weight,
            resonance_score=resonance_score,
            field_harmonics=field_harmonics
        )
    
    def _calculate_ai_direction_weight(self, state: Dict[str, float]) -> float:
        """Calculate AI direction weight based on agent roles and state."""
        return sum(state.get("agent_weights", {}).values()) * self.weight_config.direction_weight
    
    def _calculate_interaction_weight(self, interactions: List[Dict[str, float]]) -> float:
        """Calculate interaction weight based on cellular interactions."""
        if not interactions:
            return 0.0
        return sum(interaction.get("strength", 0.0) for interaction in interactions) * self.weight_config.interaction_weight
    
    def _calculate_state_weight(self, state: Dict[str, float]) -> float:
        """Calculate state weight based on current cellular state."""
        return sum(state.get("state_values", {}).values()) * self.weight_config.state_weight
    
    def _calculate_resonance_score(self, state: Dict[str, float], interactions: List[Dict[str, float]]) -> float:
        """Calculate resonance score based on state and interactions."""
        base_score = sum(state.get("resonance_values", {}).values())
        interaction_score = sum(interaction.get("resonance", 0.0) for interaction in interactions)
        return (base_score + interaction_score) * self.weight_config.resonance_weight
    
    def _calculate_field_harmonics(self, state: Dict[str, float]) -> float:
        """Calculate field harmonics based on cellular state."""
        harmonics = state.get("harmonics", {})
        return sum(harmonics.values()) * self.config["resonance"]["harmonic_scaling"]
    
    def generate_frontmatter(self, file_path: str, weights: CellularWeight) -> str:
        """Generate YAML frontmatter for markdown files."""
        frontmatter = {
            "title": os.path.basename(file_path),
            "date": datetime.now().isoformat(),
            "weights": {
                "component": weights.component_weight,
                "ai_direction": weights.ai_direction_weight,
                "interaction": weights.interaction_weight,
                "state": weights.state_weight,
                "resonance": weights.resonance_score,
                "harmonics": weights.field_harmonics
            }
        }
        return yaml.dump(frontmatter, default_flow_style=False)
    
    def update_file_weights(self, file_path: str) -> None:
        """Update weights and frontmatter for a markdown file."""
        if not file_path.endswith('.md'):
            return
        try:
            # Read existing content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            print(f"[WARNING] Skipping file due to encoding error: {file_path}")
            return
        # Calculate new weights
        weights = self.calculate_cellular_weight(
            component_type="document",
            state={"state_values": {"completion": 1.0}},
            interactions=[]
        )
        # Generate new frontmatter
        new_frontmatter = self.generate_frontmatter(file_path, weights)
        # Update file with new frontmatter
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"---\n{new_frontmatter}---\n{content}")

def ensure_frontmatter(path: pathlib.Path, meta: dict):
    """Update frontmatter with cellular AI metadata"""
    content = path.read_text(encoding='utf-8')
    if content.startswith('---'):
        _, old, body = content.split('---', 2)
    else:
        old, body = '', content
    yaml = '\n'.join(f'{k}: {v}' for k, v in meta.items())
    path.write_text(f'---\n{yaml}\n---{body}', encoding='utf-8')

def main():
    """Main entry point for weight system updates."""
    weight_system = WeightSystem()
    
    # Update weights for all markdown files
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                weight_system.update_file_weights(file_path)

if __name__ == "__main__":
    main() 