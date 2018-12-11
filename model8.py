import random
import operator
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation
import requests
import bs4

#downloading y and x data from a webpage
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)



#read the csv file and create a 2D List
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment=[]
    for row in reader:
        rowlist=[]
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
                   
         
num_of_agents = 100
num_of_iterations = 100
neighbourhood = 20
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)


# Make the agents,link them with the environment and the list of agents
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment,agents,neighbourhood, y, x))
    

carry_on = True

def update(frame_number):
    
    fig.clear() 
    global carry_on
      
    # Move the agents and make them interact with the environment and with each other
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    #plot the agents and the environment
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
def run():
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)                                                       
    canvas.show()

root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)       

tkinter.mainloop()