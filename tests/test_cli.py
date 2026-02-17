import json
import subprocess
import sys
from pathlib import Path


def test_cli_generate(tmp_path):
    input_data = {"role": "strategist", "traits": ["calm"]}
    input_file = tmp_path / "persona.json"
    input_file.write_text(json.dumps(input_data))

    result = subprocess.run(
        [sys.executable, "-m", "wlm_persona_engine.cli", "generate", str(input_file)],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    output = json.loads(result.stdout)

    assert output["role"] == "Strategist"
    assert output["traits"] == ["calm"]
