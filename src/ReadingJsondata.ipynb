{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "generating csv file:  C:\\Users\\manvi\\OneDrive\\Documents\\NLP\\business.csv\n"
     ]
    }
   ],
   "source": [
    "import argparse\n",
    "import collections\n",
    "import csv\n",
    "import json\n",
    "import codecs\n",
    "\n",
    "def get_superset_of_column_names_from_file(json_file_path):\n",
    "    \"\"\"Read in the json dataset file and return the superset of column names.\"\"\"\n",
    "    column_names = set()\n",
    "    with codecs.open(json_file_path, encoding='utf-8') as fin:\n",
    "        for line in fin:\n",
    "            line_contents = json.loads(line)\n",
    "            column_names.update(set(line_contents))\n",
    "    return column_names\n",
    "\n",
    "def read_and_write_file(json_file_path, csv_file_path, column_names):\n",
    "    \"\"\"Read in the json dataset file and write it out to a csv file, given the column names.\"\"\"\n",
    "    with open(csv_file_path, 'w',newline='') as fout:\n",
    "        csv_file = csv.writer(fout)\n",
    "        csv_file.writerow(list(column_names))\n",
    "        with codecs.open(json_file_path, encoding='utf-8') as fin:\n",
    "            for line in fin:\n",
    "                line_contents = json.loads(line)\n",
    "                csv_file.writerow(get_row(line_contents, column_names))\n",
    "                \n",
    "def get_row(line_contents, column_names):\n",
    "    \"\"\"Return a csv compatible row given column names and a dict.\"\"\"\n",
    "    row = []\n",
    "    for column_name in column_names:\n",
    "        if '.' not in column_name:\n",
    "            if column_name not in line_contents:\n",
    "                return None\n",
    "            line_value= line_contents[column_name]         \n",
    "        if isinstance(line_value, str):\n",
    "            # Convert a string that might have non-ascii chars to pure ascii string.\n",
    "            row.append(str(line_value.encode('utf-8'))[2:-1])\n",
    "        elif line_value is not None:\n",
    "            row.append('{0}'.format(line_value))\n",
    "        else:\n",
    "            row.append('')\n",
    "    return row    \n",
    "\n",
    "json_file = 'C:\\\\Users\\\\manvi\\\\OneDrive\\\\Documents\\\\NLP\\\\business.json'\n",
    "csv_file = 'C:\\\\Users\\\\manvi\\\\OneDrive\\\\Documents\\\\NLP\\\\business.csv'\n",
    "    \n",
    "print(\"generating csv file for businesses: \", csv_file)\n",
    "column_names = get_superset_of_column_names_from_file(json_file)\n",
    "read_and_write_file(json_file, csv_file, column_names)\n",
    "\n",
    "json_file = 'C:\\\\Users\\\\manvi\\\\OneDrive\\\\Documents\\\\NLP\\\\review.json'\n",
    "csv_file = 'C:\\\\Users\\\\manvi\\\\OneDrive\\\\Documents\\\\NLP\\\\review.csv'\n",
    "    \n",
    "print(\"generating csv file for reviews: \", csv_file)\n",
    "column_names = get_superset_of_column_names_from_file(json_file)\n",
    "read_and_write_file(json_file, csv_file, column_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "DishSentimentAnalysis",
   "language": "python",
   "name": "dishsentimentanalysis"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
