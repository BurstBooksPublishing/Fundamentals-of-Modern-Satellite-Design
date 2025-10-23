import torch, torch.nn as nn, torch.optim as optim
env = SimSatelliteEnv()   # simulation: orbit, battery, thermal, payload
actor = nn.Sequential(nn.Linear(env.obs_dim,64), nn.ReLU(), nn.Linear(64,env.act_dim))
critic = nn.Sequential(nn.Linear(env.obs_dim,64), nn.ReLU(), nn.Linear(64,1))
optA = optim.Adam(actor.parameters(), lr=1e-4)  # small LR for stability
optC = optim.Adam(critic.parameters(), lr=1e-3)

for episode in range(1000):
    s = env.reset()
    traj = []
    for t in range(env.max_steps):
        with torch.no_grad():
            logits = actor(torch.tensor(s,dtype=torch.float32))
            a = torch.distributions.Categorical(logits=logits).sample().item()  # discrete action
        s2, r, done, info = env.step(a)  # env computes battery, thermal, link budget
        traj.append((s,a,r,s2))
        s = s2
        if done: break
    # compute returns and update actor-critic (simple empirical returns)
    G = 0
    for s,a,r,s2 in reversed(traj):
        G = r + env.gamma * G
        v = critic(torch.tensor(s,dtype=torch.float32))
        lossC = (v - G)**2
        optC.zero_grad(); lossC.backward(); optC.step()
        advantage = (G - v).detach()
        logits = actor(torch.tensor(s,dtype=torch.float32))
        logp = torch.log_softmax(logits, dim=0)[a]
        lossA = -logp * advantage  # policy gradient with critic baseline
        optA.zero_grad(); lossA.backward(); optA.step()
# end training loop