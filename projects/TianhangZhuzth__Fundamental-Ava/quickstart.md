## 安装
需要 Python 3.11+。
```bash
git clone https://github.com/TianhangZhuzth/Fundamental-Ava.git
cd Fundamental-Ava
pip install -e ".[dev]"
```
## 最小示例
定义一个简单Settler代理，创建500个实例运行200个tick：
```python
import asyncio
from ava import Civilization, SimulationConfig
from ava.agents.base import Action, AgentCore

class Settler(AgentCore):
    async def deliberate(self, percepts, world_state):
        return Action(kind="forage", payload={"energy_cost": 1.0})

async def main():
    civ = Civilization(SimulationConfig(max_ticks=200))
    for i in range(500):
        civ.add_agent(Settler(name=f"settler-{i}", bus=civ.bus))
    reports = await civ.run()
    print(f"ran {len(reports)} ticks, final population {reports[-1].population}")

asyncio.run(main())
```
更多示例见 `experiments/role_emergence_experiment.py`。