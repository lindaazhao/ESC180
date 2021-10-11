def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    
    global last_finished
    global bored_with_stars

    global cur_star, cur_star_activity
    
    cur_hedons = 0
    cur_health = 0
    
    cur_star = None
    cur_star_activity = None
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    prev_activity_time = 0
    is_tired = False
    
    last_finished = -1000
    

            

def star_can_be_taken(activity):
    pass

    
def perform_activity(activity, duration):
    '''Simulate the user performing <activity> for <duration> minutes. duration is a positive int'''

    global cur_health, cur_hedons
    global last_activity, last_activity_duration
    global cur_star, cur_star_activity
    global cur_time

    if activity == "running":
        # Health points calculations; 3 HP / min for duration <= 180, 1 HP / min for duration > 180
        if duration <= 180:
            cur_health += 3 * duration
        if duration > 180:
            cur_health += (3 * 180) + (3 * duration - 180)

        # Hedon points calculation: 
        if cur_star and cur_star_activity == "running":
            if duration <= 10:
                cur_hedons += 2 * duration
            if duration > 10:
                cur_hedons += (2 * 10) + (-2) * (duration - 10)
            cur_star_activity = None

        last_activity = "running"

    if activity == "textbooks":
        pass

    if activity == "resting":
        pass

    else:
        pass

    cur_time += duration
    last_activity_duration = duration

def get_cur_hedons():
    pass
    
def get_cur_health():
    pass
    
def offer_star(activity):
    '''stars not given for resting, 2 stars not given at once'''
    pass
        
def most_fun_activity_minute():
    pass
    
################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

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
    
    