print('>>> starting the Program')
print('>>> Importing lib\'s')
import Data_Loader
import kmeans
import giude_gen

# define csv file path as csvFilePath Value
csvFilePath = '/home/amirahmadipg/Documents/ict6/loyal_customers/trade.csv'

# Load dataset with load_csv_data function
print('>>> Loading dataset')
df = Data_Loader.load_csv_data(csvFilePath)

# Remove outlier data's from dataset
print('>>> Clean dataset and remove ourlier data\'s')
clean_df = Data_Loader.outlier_data_remover(df)

# make train Data
print('>>> Create dataset for Training')
train_df, _ = Data_Loader.data_train_gen(clean_df, True)

# Train and save values of the kmeans dataset
print('>>> Train the algorithm')
Kmeans, centroids = kmeans.kmeans_trainer(train_df, 4)

# Define the centroid dots color
print('>>> plot data and centroids with giude')
centroids_color = ['red', 'green', 'blue', 'orange']

# Generate string for giude
guide_string = giude_gen.gen(centroids_color)

# Print the Giude String
print('>>>', guide_string)

# Plot the kmeans centroids and datas
kmeans.plot_clustur(train_df, Kmeans, centroids, centroids_color)

print('''>>> Guide 2:
    Our algorithm can detect 4 type(default) of customers:
        1- Legendary (highest),
        2- Epic (Uncommon )
        3- Rare (Good)
        3- Common''')

print(">>> end of the program")