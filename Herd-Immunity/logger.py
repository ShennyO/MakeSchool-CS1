class Logger(object):
    '''
    Utility class responsible for logging all interactions of note during the
    simulation.


    _____Attributes______

    file_name: the name of the file that the logger will be writing to.

    _____Methods_____

    __init__(self, file_name):

    write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
        basic_repro_num):
        - Writes the first line of a logfile, which will contain metadata on the
            parameters for the simulation.

    log_interaction(self, person1, person2, did_infect=None, person2_vacc=None, person2_sick=None):
        - Expects person1 and person2 as person objects.
        - Expects did_infect, person2_vacc, and person2_sick as Booleans, if passed.
        - Between the values passed with did_infect, person2_vacc, and person2_sick, this method
            should be able to determine exactly what happened in the interaction and create a String
            saying so.
        - The format of the log should be "{person1.ID} infects {person2.ID}", or, for other edge
            cases, "{person1.ID} didn't infect {person2.ID} because {'vaccinated' or 'already sick'}"
        - Appends the interaction to logfile.

    log_infection_survival(self, person, did_die_from_infection):
        - Expects person as Person object.
        - Expects bool for did_die_from_infection, with True denoting they died from
            their infection and False denoting they survived and became immune.
        - The format of the log should be "{person.ID} died from infection" or
            "{person.ID} survived infection."
        - Appends the results of the infection to the logfile.

    log_time_step(self, time_step_number):
        - Expects time_step_number as an Int.
        - This method should write a log telling us when one time step ends, and
            the next time step begins.  The format of this log should be:
                "Time step {time_step_number} ended, beginning {time_step_number + 1}..."
        - STRETCH CHALLENGE DETAILS:
            - If you choose to extend this method, the format of the summary statistics logged
                are up to you.  At minimum, it should contain:
                    - The number of people that were infected during this specific time step.
                    - The number of people that died on this specific time step.
                    - The total number of people infected in the population, including the newly
                        infected
                    - The total number of dead, including those that died during this time step.
    '''

    def __init__(self, file_name):
        # TODO:  Finish this initialization method.  The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    #We run this function right when we run our simulation to start writing the parameters of our simulation
    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       virus_spread_rate):

        f = open('%s' % self.file_name, 'w')
        # print('opened file 1:', self.file_name)
        f.write("%s people in our population, %s people got vaccinated. %s's mortality rate and spread rate are %s and %s\n" % (pop_size, vacc_percentage, virus_name, mortality_rate, virus_spread_rate))
        f.close()


        pass
    #Run this function in the exposure function I wrote, get the infected person first, pass it in this method, and keep getting person2 from the random person. Then we check if that person is infected already or if that person is vaccinated.

    def log_infected(self, person1, person2):
        with open('%s.txt' % self.file_name, 'a') as f:
            f.write("person %s infected person %s \n" % (person1._id, person2._id))

    def log_vaccinated(self, person1, person2):
        with open('%s.txt' % self.file_name, 'a') as f:
            f.write("person %s didn't infect person %s because person %s was vaccinated \n" % (person1._id, person2._id, person2._id))

    def log_already_infected(self, person1, person2):
        with open('%s.txt' % self.file_name, 'a') as f:
            f.write("person %s didn't infect person %s because person %s was already infected \n" % (person1._id, person2._id, person2._id))

    def log_not_infected(self, person1, person2):
        with open('%s.txt' % self.file_name, 'a') as f:
            f.write("person %s was not infected by person %s \n" % (person2._id, person1._id))



    # def log_interaction(self, person1, person2, did_infect=None):
    #
    #     with open('%s.txt' % self.file_name, 'a') as f:
    #     if person2.is_vaccinated:
    #
    #     if person2.infection != None:
    #         f.write("person %s didn't infect person %s because person %s was already infected" % (person1._id, person2._id))
    #     else:
    #         f.write("person %s infected pers")


        # TODO: Finish this method.  The Simulation object should use this method to
        # log every interaction a sick individual has during each time step.  This method
        # should accomplish this by using the information from person1 (the infected person),
        # person2 (the person randomly chosen for the interaction), and the optional
        # keyword arguments passed into the method.  See documentation for more info
        # on the format of the logs that this method should write.
        # NOTE:  You'll need to think
        # about how the booleans passed (or not passed) represent
        # all the possible edge cases!
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        pass
    # we run this whenever we call the unleash_infection in our person class
    def log_infection_survival(self, person):

        with open('%s.txt' % self.file_name, 'a') as f:
            if person.is_alive:
                f.write("person %s survived the infection \n" % person._id)
            else:
                f.write("person %s died from the infection \n" % person._id)


        # TODO: Finish this method.  The Simulation object should use this method to log
        # the results of every call of a Person object's .resolve_infection() method.
        # If the person survives, did_die_from_infection should be False.  Otherwise,
        # did_die_from_infection should be True.  See the documentation for more details
        # on the format of the log.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        pass
    #Log the round
    def log_time_step(self, time_step_number):
        with open('%s.txt' % self.file_name, 'a') as f:
            f.write("Time step %s ended, beginning %s... \n" % (time_step_number, time_step_number+1))


        # TODO: Finish this method.  This method should log when a time step ends, and a
        # new one begins.  See the documentation for more information on the format of the log.
        # NOTE: Stretch challenge opportunity! Modify this method so that at the end of each time
        # step, it also logs a summary of what happened in that time step, including the number of
        # people infected, the number of people dead, etc.  You may want to create a helper class
        # to compute these statistics for you, as a Logger's job is just to write logs!
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        pass
