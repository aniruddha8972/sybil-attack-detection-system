# sybil-attack-detection-system

A Sybil Attack is a form of online security violation where an entity has numerous fake identities on a blockchain for malicious reasons.
We all know any type of cyber threat causes very badly in our personal & social life. It is a severe and one of the major problem in many areas. For example, it is not much tough to rig Internet polls by using multiple IP addresses to submit votes. So, it is essential to find an optimized and controlled solution to detect the sybil attack and which is also helps us to know more about the characteristics of sybil attack in different systems like WSN, P2P & blockchain networks. WSN 's functional problems such as routing, location, data aggregation attacks are rapidly rising and become lethal threats to Networks. That’s why sybil attack is also counted as a passive attack. and It belongs in the type of network layer attack type [3]. Now come to the main point, we studied some papers & articles on some method to detect sybil attack. Some methods are really much appreciating and well effective on detecting & preventing the attack like Performance Evaluation, Resource testing, Recurring costs and fees, Trusted certification etc. But very less of those paper presented a proper algorithm or technique which can be used further in making some cyber defence-based software. We got some ideas and a blueprint that we can detect it by using the newest technology called machine Learning based method. Even if we are not the first who tried this technique. we tried to do better accuracy score of detecting the sybil attack compare to Mounica, Mandala, R. Vijayasaraswathi, and R. Vasavi published research papers. Therefore, the designed machine learning approach is to identify sybil attack based on the raw traffic internet data. We practice our machine learning model with a broad dataset, named NSLKDD_modified. The dataset named modified because when we are going to visualize the dataset, we found some drawbacks which majorly takes a part to affect the accuracy of detecting sybil attack. The details of the dataset are given below.

#NSLKDD_modified:

The NSLKDD_modified dataset is a modified dataset of the main dataset named NSLKDD. The main dataset is the type of dataset in which there are mass amount of internet traffic records were collected and bundled into a dataset called the KDD’99, and from this, the NSLKDD dataset was brought into existence, as a revised, cleaned-up version of the KDD’99 from the University of New Brunswick.
This dataset is a bundle of four sub datasets: KDDTest+, KDDTest-21, KDDTrain+, KDDTrain+_20Percent. KDDTest-21 and KDDTrain+_20 Percent are subsets of the KDDTrain+ and KDDTest+ . The KDDTest-21 is a subset of test, without the most difficult traffic records (Score of 21), and the KDDTrain+_20 Percent is a subset of train, whose record count makes up 20% of the entire train dataset.
Within the data set exists 4 different classes of attacks: Denial of Service (DoS), Probe, User to Root(U2R), and Sybil. The main reason we build a modified/advanced version of NSLKDD dataset (NSLKDD_modified) because the main train dataset named KDDTrain+ has missing some key things. When we are going to examine the dataset, we get to know that the traffic record of the sybil attack has some bias. There is a feature named protocol type in the KDDTrain+, in this feature the we see that details which has been denoted as sybil attack has only happened in the TCP protocol there are no records of UDP & ICMP protocols. But in the KDDTest+ dataset there are good number of records in UDP & ICMP protocols.
<img width="437" alt="Screenshot 2024-03-22 192024" src="https://github.com/aniruddha8972/sybil-attack-detection-system/assets/78857285/e6e9a2d5-e435-4445-9748-e6a465df3174">

In the new dataset (NSLKDD_modified) there are total 148517 network traffic data in which there are 4 main type of attacks named Dos attack, U2R attack, probe attack, and sybil attack.
We denoted these four main attacks as ordinal number system and collected it the dataset in the attack_map column like Dos attack as 1, probe attack as 2, U2R attack as 3, Sybil attack as 4 and if the network traffic details are normal then it is denoted as 0. We also add another column which basically divide the traffic as normal or attack. If the traffic details are normal then it denoted as 0 or else if it got attack then denoted as 1. In future it will help us to classify the binary predictions. From now on we denoted the NSLKDD_modified dataset as our main dataset. This dataset contains with46 columns and among them 42 are used as features and 4 are used as level or outcome of the details. Here is a pie chart for every protocol type and the attack that occurred in every protocol.
![image](https://github.com/aniruddha8972/sybil-attack-detection-system/assets/78857285/22eed105-6ae5-4a3c-ade1-e513f021d499)
                                (chart – 1: pie chart for every protocol type and the attack)
                                
Before going to our proposed model, we need to know about the flags column in the NSLKDD_modified dataset a tabular view for the description of different flags is given below.
![sc3](https://github.com/aniruddha8972/sybil-attack-detection-system/assets/78857285/2e1771a1-1d0c-44c7-848c-741da547bc78)
We use supervised learning method to accomplish our prediction model. In supervised learning, a labeled training set is used to build the system model. This model is used to represent the learned relation between the input, output, and system parameters. Here we use the first 41 columns as the features set and the last 4 columns as the label set.

#Proposed System architecture:

![sc4](https://github.com/aniruddha8972/sybil-attack-detection-system/assets/78857285/a50a0301-e86e-434b-97cc-20e25cb3d7b9)
Various examples of Supervised Learning are Strategic Regression, Decision Trees, Support vector machines, and Random Forests, and so on. As input data is fitted into the model, it adjusts to the weights until the model has been fitted appropriately, it is also occurred as part of the cross-validation process. Supervised learning helps organizations solve a variety of real-world problems at scale, such as classifying spam in a separate folder from your inbox.

#Gathering data:

Raw network traffic data involves the analysis of many attributes that utilize for prediction of the targeted level. This module involves gathering data from mass amount of internet traffic records that collected and bundled into dataset for real-time analysis. The study involves the detection of attacks in dataset records. Here we have used the NSLKDD_modified as the main resource of gathering raw internet traffic.


#Data preprocessing & feature selection:

Before deploying any machine learning model there is an essential thing we need to do. That is data preprocessing. If the dataset is missing some values or some junk values before deploying the model we need to clear those things. We may add default values provided by us in empty/missing attributes [17]. Here we also convert our categorical data into binary data. After preprocessing the data now there is a big and essential step called feature selection. In feature selection basically, we need to select the particular features to train our model and we need to select only those features that can directly cause for manipulating our accuracy score. Out of 41 features we select 9 features to train our model. Among the 9 features, there are 3 pre-encoded features and 6 later features we include to balance the accuracy score. Those features are protocol_type, service, flag, duration, src_bytes, dst_bytes, count, srv_count, logged_in.

#Model building

Algorithms are crucial in the analysis of hidden data knowledge. Because of their precision and speed, machine learning is commonly used in attack detection [8]. Here we use 4 types of supervised classification algorithms to classify the attack and get the accuracy of the model. Those are K Nearest Neighbour, Random Forest Classification, Decision Tree, and Support Vector Machine. 

# Predicted outcome
After training our model with different types of algorithms we compared our accuracy score.
Random Forest         - 98%
SVM                   - 91%
Decision Tree         - 96%

heatmaps of multiclass classification and binary classification below:

![img5](https://github.com/aniruddha8972/sybil-attack-detection-system/assets/78857285/c7f9ab30-ecde-4681-8bb9-1fea4e012390)
![img4](https://github.com/aniruddha8972/sybil-attack-detection-system/assets/78857285/707844a4-5c47-4150-93f8-8d3a76f507f6)
![img7](https://github.com/aniruddha8972/sybil-attack-detection-system/assets/78857285/a8eb81f3-b2b7-48c0-b4b2-c1ed061792af)
![img6](https://github.com/aniruddha8972/sybil-attack-detection-system/assets/78857285/f262b5fa-0989-4f2e-93db-20fc03a3f757)
However we can see that out of 930 actual Sybil attacks our machine can predict 836 of them but somehow it can’t able to predict 94 attacks (from model 91 predicted as normal, 2 as probe attack, 1 as U2R attack). We also can see that 52 normal traffic are predicted as Sybil attack. After calculating the accuracy of only Sybil attack predictions it is around 86.2% which is not so bad. 
