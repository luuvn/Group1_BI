#!/bin/bash
clear
# for ((a=0; a <= 9 ; a++))
# do
   echo "Run test..."

   ./svm_light/svm_learn ./data/svm/svm_train ./result/svm_train_model
   ./svm_light/svm_classify ./data/svm/svm_test ./result/svm_train_model ./result/predictions_model
   echo "--------------------------------"
   echo "--------------------------------"
# done
s