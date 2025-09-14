{
 "cells": [
  {
   "cell_type": "code",
<<<<<<< HEAD
   "execution_count": 16,
=======
   "execution_count": 4,
   "id": "e4f37144",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import numpy as np \n",
    "import matplotlib.pyplot as plt \n",
    "import seaborn as sns\n",
    "df=pd.read_csv('hsp_df_processed.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
>>>>>>> b5c2455d78e405d20143040c985a6504902146d8
   "id": "f0e90c12",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "# Split features and target\n",
    "X = df.drop('readmitted', axis=1)\n",
    "y = df['readmitted']\n",
    "# Train-test split\n",
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    X, y, test_size=0.2, random_state=42, stratify=y\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
<<<<<<< HEAD
   "execution_count": 17,
=======
   "execution_count": 6,
>>>>>>> b5c2455d78e405d20143040c985a6504902146d8
   "id": "727ce1f7",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'tensorflow.python.data.experimental.ops.iterator_model_ops'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[6], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mtf\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msklearn\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpreprocessing\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m LabelEncoder\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msklearn\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mmetrics\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m accuracy_score, precision_score, recall_score\n",
      "File \u001b[1;32mc:\\Users\\Kannadasan\\anaaaaaa\\Lib\\site-packages\\tensorflow\\__init__.py:55\u001b[0m\n\u001b[0;32m     53\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m autograph\n\u001b[0;32m     54\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m bitwise\n\u001b[1;32m---> 55\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m compat\n\u001b[0;32m     56\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m config\n\u001b[0;32m     57\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m data\n",
      "File \u001b[1;32mc:\\Users\\Kannadasan\\anaaaaaa\\Lib\\site-packages\\tensorflow\\_api\\v2\\compat\\__init__.py:8\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;124;03m\"\"\"Public API for tf._api.v2.compat namespace\u001b[39;00m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01msys\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01m_sys\u001b[39;00m\n\u001b[1;32m----> 8\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m v1\n\u001b[0;32m      9\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m v2\n\u001b[0;32m     10\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpython\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m forward_compatibility_horizon \u001b[38;5;66;03m# line: 125\u001b[39;00m\n",
      "File \u001b[1;32mc:\\Users\\Kannadasan\\anaaaaaa\\Lib\\site-packages\\tensorflow\\_api\\v2\\compat\\v1\\__init__.py:30\u001b[0m\n\u001b[0;32m     28\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv1\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m autograph\n\u001b[0;32m     29\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv1\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m bitwise\n\u001b[1;32m---> 30\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv1\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m compat\n\u001b[0;32m     31\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv1\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m config\n\u001b[0;32m     32\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv1\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m data\n",
      "File \u001b[1;32mc:\\Users\\Kannadasan\\anaaaaaa\\Lib\\site-packages\\tensorflow\\_api\\v2\\compat\\v1\\compat\\__init__.py:8\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;124;03m\"\"\"Public API for tf._api.v2.compat namespace\u001b[39;00m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01msys\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01m_sys\u001b[39;00m\n\u001b[1;32m----> 8\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv1\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m v1\n\u001b[0;32m      9\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv1\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m v2\n\u001b[0;32m     10\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpython\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m forward_compatibility_horizon \u001b[38;5;66;03m# line: 125\u001b[39;00m\n",
      "File \u001b[1;32mc:\\Users\\Kannadasan\\anaaaaaa\\Lib\\site-packages\\tensorflow\\_api\\v2\\compat\\v1\\compat\\v1\\__init__.py:32\u001b[0m\n\u001b[0;32m     30\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv1\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m compat\n\u001b[0;32m     31\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv1\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m config\n\u001b[1;32m---> 32\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv1\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m data\n\u001b[0;32m     33\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv1\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m debugging\n\u001b[0;32m     34\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv1\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m distribute\n",
      "File \u001b[1;32mc:\\Users\\Kannadasan\\anaaaaaa\\Lib\\site-packages\\tensorflow\\_api\\v2\\compat\\v1\\data\\__init__.py:8\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;124;03m\"\"\"Public API for tf._api.v2.data namespace\u001b[39;00m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01msys\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01m_sys\u001b[39;00m\n\u001b[1;32m----> 8\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m_api\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv2\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompat\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mv1\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mdata\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m experimental\n\u001b[0;32m      9\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpython\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mdata\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mops\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mdataset_ops\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m AUTOTUNE \u001b[38;5;66;03m# line: 103\u001b[39;00m\n\u001b[0;32m     10\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpython\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mdata\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mops\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mdataset_ops\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m DatasetV1 \u001b[38;5;28;01mas\u001b[39;00m Dataset \u001b[38;5;66;03m# line: 3710\u001b[39;00m\n",
      "File \u001b[1;32mc:\\Users\\Kannadasan\\anaaaaaa\\Lib\\site-packages\\tensorflow\\_api\\v2\\compat\\v1\\data\\experimental\\__init__.py:32\u001b[0m\n\u001b[0;32m     30\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpython\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mdata\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mexperimental\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mops\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01minterleave_ops\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m parallel_interleave \u001b[38;5;66;03m# line: 29\u001b[39;00m\n\u001b[0;32m     31\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpython\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mdata\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mexperimental\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mops\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01minterleave_ops\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m sample_from_datasets_v1 \u001b[38;5;28;01mas\u001b[39;00m sample_from_datasets \u001b[38;5;66;03m# line: 158\u001b[39;00m\n\u001b[1;32m---> 32\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpython\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mdata\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mexperimental\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mops\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01miterator_model_ops\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m get_model_proto \u001b[38;5;66;03m# line: 25\u001b[39;00m\n\u001b[0;32m     33\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpython\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mdata\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mexperimental\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mops\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01miterator_ops\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m make_saveable_from_iterator \u001b[38;5;66;03m# line: 38\u001b[39;00m\n\u001b[0;32m     34\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpython\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mdata\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mexperimental\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mops\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mlookup_ops\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m DatasetInitializer \u001b[38;5;66;03m# line: 54\u001b[39;00m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'tensorflow.python.data.experimental.ops.iterator_model_ops'"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.metrics import accuracy_score, precision_score, recall_score\n",
    "import numpy as np\n",
    "# Ensure y is numeric (0/1)\n",
    "encoder = LabelEncoder()\n",
    "y_train_enc = encoder.fit_transform(y_train)\n",
    "y_test_enc = encoder.transform(y_test)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "4eefae35",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "# Convert categorical columns to one-hot encoding\n",
    "X = pd.get_dummies(X, drop_first=True)\n",
    "# Split again\n",
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    X, y, test_size=0.2, random_state=42, stratify=y\n",
    ")\n",
    "# Encode target\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "encoder = LabelEncoder()\n",
    "y_train_enc = encoder.fit_transform(y_train)\n",
    "y_test_enc = encoder.transform(y_test)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "ef6b881c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m5s\u001b[0m 7ms/step - accuracy: 0.6323 - loss: 0.6377 - val_accuracy: 0.6078 - val_loss: 0.6655\n",
      "Epoch 2/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m5s\u001b[0m 8ms/step - accuracy: 0.6262 - loss: 0.6379 - val_accuracy: 0.6098 - val_loss: 0.6650\n",
      "Epoch 3/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 5ms/step - accuracy: 0.6223 - loss: 0.6402 - val_accuracy: 0.6110 - val_loss: 0.6681\n",
      "Epoch 4/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m4s\u001b[0m 6ms/step - accuracy: 0.6265 - loss: 0.6356 - val_accuracy: 0.6048 - val_loss: 0.6707\n",
      "Epoch 5/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 5ms/step - accuracy: 0.6317 - loss: 0.6348 - val_accuracy: 0.6010 - val_loss: 0.6762\n",
      "Epoch 6/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 4ms/step - accuracy: 0.6375 - loss: 0.6265 - val_accuracy: 0.6164 - val_loss: 0.6672\n",
      "Epoch 7/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 5ms/step - accuracy: 0.6408 - loss: 0.6260 - val_accuracy: 0.6116 - val_loss: 0.6715\n",
      "Epoch 8/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 4ms/step - accuracy: 0.6386 - loss: 0.6270 - val_accuracy: 0.6108 - val_loss: 0.6699\n",
      "Epoch 9/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 4ms/step - accuracy: 0.6304 - loss: 0.6300 - val_accuracy: 0.6030 - val_loss: 0.6845\n",
      "Epoch 10/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 4ms/step - accuracy: 0.6388 - loss: 0.6274 - val_accuracy: 0.6056 - val_loss: 0.6746\n",
      "Epoch 11/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 4ms/step - accuracy: 0.6414 - loss: 0.6229 - val_accuracy: 0.6094 - val_loss: 0.6750\n",
      "Epoch 12/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 5ms/step - accuracy: 0.6391 - loss: 0.6231 - val_accuracy: 0.6044 - val_loss: 0.6744\n",
      "Epoch 13/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 5ms/step - accuracy: 0.6441 - loss: 0.6206 - val_accuracy: 0.5998 - val_loss: 0.6832\n",
      "Epoch 14/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 4ms/step - accuracy: 0.6403 - loss: 0.6208 - val_accuracy: 0.5992 - val_loss: 0.6849\n",
      "Epoch 15/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 5ms/step - accuracy: 0.6451 - loss: 0.6208 - val_accuracy: 0.6152 - val_loss: 0.6809\n",
      "Epoch 16/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 5ms/step - accuracy: 0.6495 - loss: 0.6155 - val_accuracy: 0.6066 - val_loss: 0.6866\n",
      "Epoch 17/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 5ms/step - accuracy: 0.6456 - loss: 0.6126 - val_accuracy: 0.6030 - val_loss: 0.6845\n",
      "Epoch 18/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 5ms/step - accuracy: 0.6520 - loss: 0.6148 - val_accuracy: 0.6026 - val_loss: 0.6911\n",
      "Epoch 19/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 4ms/step - accuracy: 0.6445 - loss: 0.6143 - val_accuracy: 0.6000 - val_loss: 0.6921\n",
      "Epoch 20/20\n",
      "\u001b[1m625/625\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 4ms/step - accuracy: 0.6567 - loss: 0.6024 - val_accuracy: 0.6074 - val_loss: 0.6940\n"
     ]
    }
   ],
   "source": [
    "# Ensure numeric dtype\n",
    "X_train = X_train.astype('float32')\n",
    "X_test = X_test.astype('float32')\n",
    "\n",
    "y_train_enc = y_train_enc.astype('int32')\n",
    "y_test_enc = y_test_enc.astype('int32')\n",
    "# Now train\n",
    "history = model.fit(\n",
    "    X_train, y_train_enc,\n",
    "    epochs=20,\n",
    "    batch_size=32,\n",
    "    validation_data=(X_test, y_test_enc),\n",
    "    verbose=1\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "19730b9e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/20\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\Users\\jeni7\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\keras\\src\\layers\\core\\dense.py:87: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.\n",
      "  super().__init__(activity_regularizer=activity_regularizer, **kwargs)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 5ms/step - accuracy: 0.5423 - loss: 0.7357 - val_accuracy: 0.6003 - val_loss: 0.6628\n",
      "Epoch 2/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 4ms/step - accuracy: 0.5963 - loss: 0.6688 - val_accuracy: 0.5763 - val_loss: 0.7197\n",
      "Epoch 3/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 4ms/step - accuracy: 0.6009 - loss: 0.6722 - val_accuracy: 0.5673 - val_loss: 0.6872\n",
      "Epoch 4/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 3ms/step - accuracy: 0.6022 - loss: 0.6629 - val_accuracy: 0.6015 - val_loss: 0.6664\n",
      "Epoch 5/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 5ms/step - accuracy: 0.6033 - loss: 0.6588 - val_accuracy: 0.6033 - val_loss: 0.6633\n",
      "Epoch 6/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 5ms/step - accuracy: 0.6083 - loss: 0.6571 - val_accuracy: 0.6025 - val_loss: 0.6602\n",
      "Epoch 7/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m4s\u001b[0m 7ms/step - accuracy: 0.6160 - loss: 0.6525 - val_accuracy: 0.6135 - val_loss: 0.6563\n",
      "Epoch 8/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 5ms/step - accuracy: 0.6153 - loss: 0.6541 - val_accuracy: 0.5918 - val_loss: 0.6669\n",
      "Epoch 9/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 4ms/step - accuracy: 0.6192 - loss: 0.6480 - val_accuracy: 0.6070 - val_loss: 0.6612\n",
      "Epoch 10/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 5ms/step - accuracy: 0.6200 - loss: 0.6515 - val_accuracy: 0.5993 - val_loss: 0.6634\n",
      "Epoch 11/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 4ms/step - accuracy: 0.6192 - loss: 0.6473 - val_accuracy: 0.6050 - val_loss: 0.6582\n",
      "Epoch 12/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 5ms/step - accuracy: 0.6190 - loss: 0.6507 - val_accuracy: 0.6020 - val_loss: 0.6608\n",
      "Epoch 13/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 4ms/step - accuracy: 0.6213 - loss: 0.6491 - val_accuracy: 0.6072 - val_loss: 0.6587\n",
      "Epoch 14/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 5ms/step - accuracy: 0.6270 - loss: 0.6442 - val_accuracy: 0.6030 - val_loss: 0.6588\n",
      "Epoch 15/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 5ms/step - accuracy: 0.6326 - loss: 0.6394 - val_accuracy: 0.6105 - val_loss: 0.6565\n",
      "Epoch 16/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 4ms/step - accuracy: 0.6230 - loss: 0.6422 - val_accuracy: 0.5980 - val_loss: 0.6678\n",
      "Epoch 17/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 3ms/step - accuracy: 0.6225 - loss: 0.6423 - val_accuracy: 0.6060 - val_loss: 0.6619\n",
      "Epoch 18/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 4ms/step - accuracy: 0.6326 - loss: 0.6352 - val_accuracy: 0.6037 - val_loss: 0.6660\n",
      "Epoch 19/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 6ms/step - accuracy: 0.6265 - loss: 0.6395 - val_accuracy: 0.6040 - val_loss: 0.6618\n",
      "Epoch 20/20\n",
      "\u001b[1m500/500\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 4ms/step - accuracy: 0.6346 - loss: 0.6350 - val_accuracy: 0.6025 - val_loss: 0.6654\n"
     ]
    }
   ],
   "source": [
    "# Build model\n",
    "model = tf.keras.models.Sequential([\n",
    "    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),\n",
    "    tf.keras.layers.Dense(32, activation='relu'),\n",
    "    tf.keras.layers.Dense(1, activation='sigmoid')\n",
    "])\n",
    "# Compile model\n",
    "model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])\n",
    "# Train model\n",
    "history = model.fit(X_train, y_train_enc, epochs=20, batch_size=32, validation_split=0.2, verbose=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "72c1130c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m157/157\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 2ms/step\n",
      "Testing Accuracy: 0.6028\n",
      "Precision: 0.5739165654110976\n",
      "Recall: 0.6027222458528286\n"
     ]
    }
   ],
   "source": [
    "# Predictions\n",
    "y_pred_prob = model.predict(X_test)\n",
    "y_pred = (y_pred_prob > 0.5).astype(int).flatten()\n",
    "# Metrics\n",
    "print(\"Testing Accuracy:\", accuracy_score(y_test_enc, y_pred))\n",
    "print(\"Precision:\", precision_score(y_test_enc, y_pred))\n",
    "print(\"Recall:\", recall_score(y_test_enc, y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54c017d4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d34ffb7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
