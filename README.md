To run use "python run.py [OPTIONS]". Only dependency is on segan.jar which can be checked out and built from https://github.com/vietansegan/segan, and should be in the folder BASE_DIR/segan/dist/segan.jar.  Also, if the weka classifier is to be used, uncomment out the relevant lines near the end of run.py and redirect to appropriate jar file. Other global variables may need to be changed near the top of the file but most are set with input parameters.

Example command to run 50-topic LDA prior then SLDA:

python run.py -in_tag train -ne lda -ne_run -ne_pp -predict -pred_set dev -prior -tw slda -tw_pp -tw_run --k 5 -vocab vocab.txt --neuro input/in_file1.txt -in_file input/in_file2

This runs lda on the data in input/in_file1.txt then uses that as a prior for slda training on the text from input/in_file2.train.txt (note for training and testing it assumes the file given to the "-in_file" parameter is actually followd by "train.txt" for the training set and "dev.txt" for the testing set. If supervised labels are used the label files should be named [in_file].train.lbl and [in_file].dev.lbl) and prediction on the text in input/in_file2.dev.txt. It uses the vocabulary in vocab.txt, which is an alphabetized whitelist of words (tokens) to consider, 1 token per line.  The input files are a list of documents, 1 document per line, in the format "[id]\t[document]" where [id] is the document id, and [document] is a space separated list of words in the document. The label files (if any) are of the format "[id]\t[label]" where [id] should match the document corresponding to the label in the text file.

By default output is sent to BASE_DIR/output/_[timestamp], but can be further labeled with the -out_tag parameter, or set explicitly with the -model_dir parameter.  Output is in the same format as in https://github.com/vietansegan/segan, with some additional utility files in the root of the output directory.

The code/ directory contains both python scripts used by run.py and a few additional utilities for preprocessing data or extracting results.
