# Momentum is conserved when the total initial momentum is equal to the total final momentum of a system.
# Elastic collision is a collision such that no energy is lost to the surrounding.

# Write a function for an elastic collision, that takes in the masses and the initial velocities of two bodies ,
# and return the respective final velocities of the two bodies.

def collision(m1,v1,m2,v2):
  
  nett_mom = m1*v1 + m2*v2
  
  return v1, v2
