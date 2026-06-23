def job_completed():
    print("Job completed successfully!")

def do_job(callback):
    print("Processing the job...")
    
    # Simulating job execution
    print("Job is running...")
    
    callback()  # Call the callback function

do_job(job_completed)