convert2singlefile.py
========
**Ryan M. Bergmann, Paul Scherrer Institut, Nov. 10, 2014.**

Python script to convert newer MCNP inputs which have 'read file' cards into a single file for use with MCNPX 2.4.0, which is openly distributed. Can be useful in situations where people are waiting for license approval.

USAGE:

input_file:   name of file to consilidate, required
output_file:  name of written outputfile, optional

``` bash
$ ./convert2singlefile.py input_file [output_file]
```