char.1<-c("F","M","F","F","M","F","M","F","M","F")
factor.1<-factor(char.1)
factor.1
levels(factor.1)<-c("Female", "Male")
factor.1
factor(char.1,levels=c("M", "F"),labels=c("Male", "Female"))
char.1A<-c(1,2,1,1,2,1,2,1,2,1) # numeric vector to indicate gender
factor(char.1A,levels=c(1,2),labels=c("Female", "Male"))

num.v<-c(1,3,4.1,5,6.1,8,9,10.11,30,5.3)
mat.num.1<-matrix(num.v,nrow=2,ncol=5) # matrix filled by columns
mat.num.1

mat.num.2<-matrix(num.v,nrow=2,ncol=5,byrow=T) # matrix filled by rows
mat.num.2

num.2A<-c(1,3,4.1,5,6.1)
num.2B<-c(8,9,10.11,30,5.3)

mat.num.2<-rbind(num.2A,num.2B) # obtained by overlapping The two vectors by row
mat.num.2

mat.num.3<-matrix(c(1:3,21:23,1,120,240,5,9,12),nrow=3,ncol=4)
mat.num.3

mat.num.3<-cbind(1:3,21:23,c(1,120,240),c(5,9,12)) # bind vectors
mat.num.3
dim(mat.num.3)
colnames(mat.num.3)=c("First Column", "Second Column", "Third Column", "Fourth Column")
rownames(mat.num.3)=c("First Row", "Second Row", "Third Row")
colSums(mat.num.3)

Loyalty$Amount_V <- Loyalty$Amount/Loyalty$Nr_visits
Loyalty$Recommend.F<-factor(Loyalty$Recommend,levels=c("Very Unlikely", "Unlikely", "Neutral","Likely,", "Very Likely"))

factor(Loyalty$Recommend)
factor(Loyalty$Recommend.F)


mat<-matrix(1:16,nrow=4)
vecnum <- c(1,10,12,20)
vecstring<-c("Male", "Female", "Female", "Male")
fact<-factor(c(1,1,1,4))
levels(fact)<-c("North", "South")
veclogic <- (vecstring=="Male" & fact=="North")
df1 <- data.frame(vecstring,fact,veclogic,vecnum,mat)
df1
