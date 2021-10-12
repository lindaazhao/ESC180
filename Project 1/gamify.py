def initialize():
    '''Initialize the global variables needed for the simulation.'''
    
    # Stores the current number of hedons, health the user has
    # Integer >= 0
    global cur_hedons, cur_health

    # Stores the cumulative time passed since the simulation started
    # Integer >= 0
    global cur_time

    global last_activity, last_activity_duration # Haven't used these

    # Stores the most recent time (provided by cur_time) at which textbooks 
    # or running was performed
    # None to begin, integer > 0 after first activity is performed
    global prev_activity_time
    
    # Stores whether or not the user has taken 3+ stars in 2 hours (bored)
    # Boolean
    global bored_with_stars
    
    # Stores times at which stars were offered to the user (using cur_time)
    # Array, indexes are integers >= 0
    global star_times

    global cur_star, cur_star_activity
    
    cur_hedons = 0
    cur_health = 0
    
    cur_star = None
    cur_star_activity = None
    
    star_times = []
    bored_with_stars = False
    
    last_activity = None # Haven't used this
    last_activity_duration = 0 # Or this
    
    cur_time = 0
    prev_activity_time = None   
    
def is_tired():
    '''Return True if user performed running or textbooks in last 120 mins.'''
    return prev_activity_time is not None \
    and cur_time - prev_activity_time < 120
            

def star_can_be_taken(activity):
    '''Return True if a star can be used to boost hedons for <activity>,
    otherwise return False.
    Assume <activity> is "running" or "textbooks."'''
    return cur_star_activity == activity and not bored_with_stars

    
def perform_activity(activity, duration):
    '''Simulate the user performing <activity> for <duration> minutes. 
    Return None.
    Assume <duration> is a positive int.'''

    global cur_health, cur_hedons
    global last_activity, last_activity_duration, prev_activity_time
    global cur_star, cur_star_activity
    global cur_time

    if activity == "running":
        # Health points: 3 HP / min for duration <= 180
        # 1 HP / min for each min of duration > 180
        if duration <= 180:
            cur_health += 3 * duration
        if duration > 180:
            cur_health += (3 * 180) + (duration - 180)

        # Hedons
        if not is_tired():
            if duration <= 10:
                cur_hedons += 2 * duration
            else: # If duration > 10
                cur_hedons += (2 * 10) + (-2) * (duration - 10)
        else: # is_tired()
            cur_hedons += (-2) * duration

        # last_activity = "running"

    if activity == "textbooks":
        # Health points: Always 2 HP / min
        cur_health += 2 * duration

        # Hedons
        if not is_tired():
            if duration <= 20:
                cur_hedons += 1 * duration
            else: # If duration > 20
                cur_hedons += (20) - (duration - 20)
        else: # is_tired()
            cur_hedons += (-2) * duration

        # last_activity = "textbooks"

    # if activity == "resting":
    #     last_activity = "resting"

    if star_can_be_taken(activity):
        cur_hedons += 3 * min(duration, 10)

    cur_star_activity = None
    cur_time += duration
    if activity == "running" or activity == "textbooks":
        prev_activity_time = cur_time
    # last_activity_duration = duration

def get_cur_hedons():
    '''Return the current number of hedons that the user has 
    in the current simulation.'''
    return cur_hedons
    
def get_cur_health():
    '''Return the current number of health points that the user has 
    in the current simulation.'''
    return cur_health

# Completed; gives a star for <activity>, documents the time it was given,
# Checks if the user is bored with stars and updates star_times
def offer_star(activity):
    '''Simulate offering the user a star for <activity>.
    Assume stars not given for resting, 2 stars not given at once.
    Assume <activity> is "running" or "textbooks".'''
    global cur_star_activity
    global bored_with_stars

    cur_star_activity = activity
    star_times.append(cur_time)

    if len(star_times) >= 3:
        if star_times[2] - star_times[0] < 120:
            bored_with_stars = True
        star_times.pop(0) 
   
def most_fun_activity_minute():
    pass
    
################################################################################
#These functions are not required, but we recommend that you use them anyway as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass
    
def get_effective_minutes_left_health(activity):
    pass    

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass
            

def estimate_health_delta(activity, duration):
    pass
        
################################################################################
        
if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)    
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)  
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
    
    