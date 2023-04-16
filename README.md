# academicProfileSyncer

---

# academicProfileSyncer's  subsystems 

    uniparser parses the universities' lessons and teachers 
    instructorParser gathers instructor's published papers
    instructorCorrelater correlates instructor's abilities to teach that lesson with the instructor's papers
    profileServer hosts instructors' profiles 
    SyncedProfile is an extension that tags all the known teachers in the current website to a link to instructor's profile   

---
## Cold start
download pipreqs 
    ```
        pip3 install pipreqs
 
    ```

create a virtual environment with 
    ```
        python3 -m venv 
    ```
    
activate the environment on linux 
    ```
        source venv/bin/activate
    ```
    
install all dependencies
    ```
        pip3 install --upgrade -r requirements.txt
    ```

---
# uniParser
## Data parsing tool that gathers courses and instructors for Turkish computer science departments.

---

to generating csv file use
    ```
        python3 main.py
    ```

---


---
# instructorParser
## Data parsing tool that gathers instructor's published papers

---


## Cold start
    create a virtual environment with 
    ```
        python3 -m venv 
    ```
    then activate the environment on linux 
    ```
        source venv/bin/activate
    ```
    use to install all dependencies
    ```
        pip3 install requirement.txt
    ```

    then run to generate csv file
    ```
        python3 main.py
    ```

---
## before pushing commit
    freeze your dependencies 
    ```
        pipreqs --force
    ```