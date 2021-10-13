def initialize():
    '''Initialize the global variables needed for the simulation.'''
    
    # Stores the current number of hedons, health the user has
    # Integer >= 0
    global cur_hedons, cur_health

    # Stores the cumulative time passed since the simulation started
    # Integer >= 0
    global cur_time

    # Stores the most recent time (provided by cur_time) at which textbooks 
    # or running was performed
    # None to begin, integer > 0 after first activity is performed
    global prev_tiring_activity_time
    
    # Stores whether or not the user has taken 3+ stars in 2 hours (bored)
    # Boolean
    global bored_with_stars
    
    # Stores times at which stars were offered to the user (using cur_time)
    # Array, indexes are integers >= 0
    global star_times

    # Stores the activity that a star was most recently offered for, resets
    # after any activity is performed
    # String = "running" or "textbooks"
    global cur_star_activity

    # Stores the value of these variables at a certain point in the simulation
    # so they can be recalled and used later
    global save_star_activity, save_cur_hedons, save_cur_health
    
    cur_hedons = 0
    cur_health = 0
    
    cur_star_activity = None
    
    star_times = []
    bored_with_stars = False
    
    cur_time = 0
    prev_tiring_activity_time = None   
    

def is_tired():
    '''Return True if user is tired, 
    i.e. performed running or textbooks in last 120 mins.'''
    return prev_tiring_activity_time is not None \
        and cur_time - prev_tiring_activity_time < 120
            

def star_can_be_taken(activity):
    '''Return True iff a star can be used to boost hedons for <activity>,
    otherwise return False.
    Assume <activity> is "running" or "textbooks".'''
    # FAQ 1.6: Assume stars will not be given for resting.
    return cur_star_activity == activity and not bored_with_stars and \
        activity != "resting"


def perform_activity(activity, duration):
    '''Simulate the user performing <activity> for <duration> minutes. 
    Return None.
    Assume <duration> is a positive int.'''

    global cur_health, cur_hedons
    global last_activity, last_activity_duration, prev_tiring_activity_time
    global cur_star_activity
    global cur_time

    # Nothing happens if <activity> is not one of the 3 listed activities.
    if activity == "running" or \
        activity == "resting" or \
        activity == "textbooks":

        if activity == "running":
            # Health points: 3 HP / min for duration <= 180
            # 1 HP / min for each min of duration > 180
            if duration <= 180:
                cur_health += 3 * duration
            if duration > 180:
                cur_health += (3 * 180) + (duration - 180)

            # Hedons: 2 / min for duration <= 10, 
            # -2 / min for each min of duration > 10, -2 / min if tired
            if not is_tired():
                if duration <= 10:
                    cur_hedons += 2 * duration
                else: # If duration > 10
                    cur_hedons += (2 * 10) + (-2) * (duration - 10)
            else: # is_tired()
                cur_hedons += (-2) * duration

        if activity == "textbooks":
            # Health points: Always 2 HP / min
            cur_health += 2 * duration

            # Hedons: 1 / min for duration <= 20, 
            # -1 / min for each min of duration > 20, -2 / min if tired
            if not is_tired():
                if duration <= 20:
                    cur_hedons += 1 * duration
                else: # If duration > 20
                    cur_hedons += (20) - (duration - 20)
            else: # is_tired()
                cur_hedons += (-2) * duration

        if star_can_be_taken(activity):
            cur_hedons += 3 * min(duration, 10)

        cur_star_activity = None
        cur_time += duration
        if activity == "running" or activity == "textbooks":
            prev_tiring_activity_time = cur_time


def get_cur_hedons():
    '''Return the current number of hedons that the user has 
    in the current simulation.'''
    return cur_hedons


def get_cur_health():
    '''Return the current number of health points that the user has 
    in the current simulation.'''
    return cur_health


def offer_star(activity):
    '''Simulate offering the user a star for <activity>.
    Assume 2 stars are not given at once and that <activity> is 
    "running" or "textbooks".'''
    # FAQ 1.5: Assume two stars will not be given at once.
    # FAQ 1.6: Assume stars will not be given for resting.
    global cur_star_activity
    global bored_with_stars

    cur_star_activity = activity
    # Document the time the star was offered
    star_times.append(cur_time)

    # Check if the user is bored with stars (i.e. 3+ stars have been 
    # offered within 120 min) and update star_times
    if len(star_times) >= 3:
        if star_times[2] - star_times[0] < 120:
            bored_with_stars = True
        # Remove the first star_time to keep the list to a maximum of 3 items
        star_times.pop(0)


def save_current_state():
    '''Save the current state of the simulation in terms of 
    cur_star_activity, cur_hedons, and cur_health'''
    global cur_star_activity, cur_hedons, cur_health
    global save_star_activity, save_cur_hedons, save_cur_health

    # Save the activity a star was most recently offered for
    save_star_activity = cur_star_activity
    # Save the current # of hedons the user has
    save_cur_hedons = cur_hedons
    # Save the current # of health points the user has
    save_cur_health = cur_health


def reset_minute_activity():
    '''Reset simulation variables to the previous state saved by 
    save_current_state()'''
    global cur_star_activity, cur_hedons, cur_health
    global save_star_activity, save_cur_hedons, save_cur_health

    # Reset cur_star_activity, cur_hedons and cur_health to previously saved 
    # state using save_current_state()
    cur_star_activity = save_star_activity
    cur_hedons = save_cur_hedons
    cur_health = save_cur_health   

   
def most_fun_activity_minute():
    '''Return an activity "running", "textbooks", or "resting" that would give 
    the most hedons if performed for 1 minute at the current time'''
    save_current_state()

    perform_activity("running", 1)
    # Calculate hedons gained from 1 min of running
    running_hedons = cur_hedons - save_cur_hedons
    # Reset simulation to previous state, before 1 minute of running
    reset_minute_activity() 

    perform_activity("textbooks", 1)
    textbooks_hedons = cur_hedons - save_cur_hedons
    reset_minute_activity()

    resting_hedons = 0 # Resting always provides 0 hedons

    if running_hedons > textbooks_hedons and running_hedons > resting_hedons:
        return "running"
    elif textbooks_hedons > running_hedons and \
        textbooks_hedons > resting_hedons:
        return "textbooks"
    else:
        return "resting"

        
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
    print(get_cur_health())            # 720 = 210 + 170 * 3                  # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
    
    