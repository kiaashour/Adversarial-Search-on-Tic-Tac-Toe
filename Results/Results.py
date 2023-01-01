#Import packages
import pandas as pd
import numpy as np
import AlphaBeta
import MinMax

#Get results for the MinMax and AlphaBeta algorithms
if __name__ == "__main__":
    #Also getting the average time and states visited for different values of m,n,k
    #where m=2,3,4, n=2,3,4, k=2,3,4. Doing this for Alpha-Beta pruning and MinMax.

    #Create pandas dataframe with columns m,n,k, avg_time, avg_states_visited
    df_minmax = pd.DataFrame(columns=['m', 'n', 'k', 'avg_time', 'avg_states_visited'])
    df_alphabeta = pd.DataFrame(columns=['m', 'n', 'k', 'avg_time', 'avg_states_visited'])
    runs = 3   #number of runs to average


    for m in range(2,5):
        for n in range(2,5):
            for k in range(2,5):
                if k <= m or k <= n:                
                    
                    #Averaging over "runs" games:
                    times_minmax = []
                    states_visited_minmax = []
                    times_alphabeta = []
                    states_visited_alphabeta = []
                    for i in range(runs):

                        #For Alpha-Beta pruning
                        tictactoe_ab = AlphaBeta.Game(m, n, k, display=False)
                        tictactoe_ab.initialize_game()
                        tictactoe_ab.play()
                        print("Average time taken for m={}, n={}, k={} is {}".format(m, n, k, np.mean(tictactoe_ab.times)))
                        print("Average states visited for m={}, n={}, k={} is {}".format(m, n, k, tictactoe_ab.states_visited))
                        times_alphabeta.append(np.mean(tictactoe_ab.times))
                        states_visited_alphabeta.append(tictactoe_ab.states_visited)

                        #For MinMax
                        tictactoe_mm = MinMax.Game(m, n, k, display=False)
                        tictactoe_mm.initialize_game()
                        tictactoe_mm.play()
                        print("Average time taken for m={}, n={}, k={} is {}".format(m, n, k, np.mean(tictactoe_mm.times)))
                        print("Average states visited for m={}, n={}, k={} is {}".format(m, n, k, tictactoe_mm.states_visited))
                        times_minmax.append(np.mean(tictactoe_mm.times))
                        states_visited_minmax.append(tictactoe_mm.states_visited)         

                    #Store the average times and states visited for minmax and alphabeta in the dataframe
                    df_minmax = df_minmax.append({'m': m, 'n': n, 'k': k, 'avg_time': np.mean(times_minmax), 'avg_states_visited': np.mean(states_visited_minmax)}, ignore_index=True)
                    df_alphabeta = df_alphabeta.append({'m': m, 'n': n, 'k': k, 'avg_time': np.mean(times_alphabeta), 'avg_states_visited': np.mean(states_visited_alphabeta)}, ignore_index=True)

                    #Export the dataframes to csv after each run
                    df_minmax.to_csv('minmax_results.csv')
                    df_alphabeta.to_csv('alphabeta_results.csv')        

                
