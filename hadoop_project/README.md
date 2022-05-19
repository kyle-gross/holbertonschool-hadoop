# Hadoop project

## Resources

* [Install Hadoop WSL2](https://tecadmin.net/install-hadoop-on-ubuntu-20-04/ "Install Hadoop WSL2")
* [Top 10 Hadoop Commands](https://data-flair.training/blogs/top-hadoop-hdfs-commands-tutorial/ "Top 10 Hadoop Commands")
* [hadoop fs VS. hdfs dfs](https://intellipaat.com/community/42860/hadoop-fs-or-hdfs-dfs-and-whats-the-difference#:~:text=There%20IS%20a%20difference%20between,on%20external%20platforms%20as%20well. "hadoop fs VS. hdfs dfs")
* [MapReduce book](http://lintool.github.io/MapReduceAlgorithms/ed1n/MapReduce-algorithms.pdf "MapReduce book")
* [MapReduce Tutorial](https://www.softwaretestinghelp.com/hadoop-mapreduce-tutorial/ "MapReduce Tutorial")

## References

* [snakebite.client.Client](https://snakebite.readthedocs.io/en/latest/client.html "snakebite.client.Client")

## Tasks

Running any of these files requires an active Hadoop cluster on the local machine.

### [0. HDFS with BASH (1)]( "0. HDFS with BASH (1)")

Bash script which creates directories within HDFS.

Run with:

```bash
$ ./createdirectories.sh
```

### [1. HDFS with BASH (2)]( "1. HDFS with BASH (2)")

Bash script which uploads the file `lao.txt` to the `/holbies/input` directory on the HDFS.

Run with:

```bash
$ ./lao.sh
```

### [2. HDFS with BASH (3)]( "2. HDFS with BASH (3)")

Bash script that displays the contents of `lao.txt` from the HDFS.

Run with:

```bash
$ ./text.sh
```

### [3. HDFS with Python (Snakebite): createdir]( "3. HDFS with Python (Snakebite): createdir")

Python script which creates directories on the HDFS.

Run with:

```bash
$ ./4-createdir.py
```

### [4. HDFS with Python (Snakebite): deletedir]( "4. HDFS with Python (Snakebite): deletedir")

Python script which deleted directories on the HDFS.

Run with:

```bash
$ ./5-deletedir.py
```

### [5. HDFS with Python (Snakebite): download]( "5. HDFS with Python (Snakebite): download")

Python script that retrieves files listed in `l` and stores them in the `/home/tmp` directory of the user.

Run with:

```bash
$ ./6-download.py
```

### [6. MapReduce (mapper)]( "6. MapReduce (mapper)")

The mapper function for the MapReduce function. Displays relevant content of the csv file to stdout for the reducer function.

Run with:

```bash
$ cat salaries.csv | ./mapper.py
```

### [7. MapReduce (reducer)]( "7. MapReduce (reducer)")

The reducer function for the MapReduce function. Displays the top 10 highest salaries with their companies.

Run with:

```bash
$ cat salaries.csv | ./mapper.py | ./reducer.py
```
