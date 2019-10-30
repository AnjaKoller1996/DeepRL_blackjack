import gym


class BlackJackRandomAgent():
    def __init__(self, num_episodes=1):

        self.env = gym.make('Blackjack-v0')
        # Variable to store all the possible actions of the environment
        nA = self.env.action_space.n
        nS = self.env.observation_space
        print('na', nA)
        print('ns', nS)

    def choose_random_action(self, state):
        # randomly sample
        return self.env.action_space.sample()


    def run(self):
        self.env = gym.make('Blackjack-v0')

        while True:
            current_state = self.env.reset()
            done = False

            while not done:
                action = self.choose_random_action(current_state)
                obs, reward, done, _ = self.env.step(action)
                # print('state', obs)e
                # update state to newstate
                current_state = obs
            print('finished run with reward', reward);




if __name__ == "__main__":
    agent = BlackJackRandomAgent()
    # no training necessary as this is the random strategy
    agent.run()
