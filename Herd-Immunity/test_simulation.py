import pytest
from simulation import Simulation
import random
random.seed(42)

#self.population_size = population_size
# self.initially_infected = initially_infected
# self.virus_name = virus_name
# self.virus_mortality_rate = virus_mortality_rate
# self.virus_spread_rate = virus_spread_rate
# self.initial_vaccinated_percentage = initial_vaccinated_percentage
# self.population = []

# self.file_name = "epidemic.txt"

def set_up_test():
    sim = Simulation(300, 50, "Malaria", .30, .15, .25)
    pop = sim.create_population()
    return [sim, pop]

def test_init():
    sim = set_up_test()
    assert sim[0].population_size == 300
    assert sim[0].initially_infected == 50
    assert sim[0].virus_name == "Malaria"
    assert sim[0].virus_mortality_rate == .30
    assert sim[0].virus_spread_rate == .15
    assert sim[0].initial_vaccinated_percentage == .25
    assert sim[0].population == []
    assert sim[0].file_name == "epidemic.txt"

def test_create_population():
    sim = set_up_test()

    #[self.population, infected_count, vaccinated_count, not_vacc]
    assert sim[1][0] == 300
    assert sim[1][1] == 50
    assert sim[1][2] == 71
    assert sim[1][3] == 179


def test_exposure():
    sim = set_up_test()
    sim.create_population()
    round_1 = sim.exposure()

    assert round_1[0] == 166
    assert round_1[1] == 71
    assert round_1[2] == 63

    #[non_vac, _vaccinated, _infected]
    # 166 are not vaccinated
    # 71 are vaccinated
    # 0 are dead
    # 63 are infected
