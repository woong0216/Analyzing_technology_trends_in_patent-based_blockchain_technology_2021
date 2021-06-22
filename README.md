# Analyzing technology trends in patent-based blockchain technology redefining processes

## Background
- It was created on January 3, 2009 by Nakamoto Satoshi.
- During 2018-2019 the representative technology of blockchain is based on Distributed ledger technology (DLT).
- Bitcoin has declined since an explosive increase in 2018, but it is still in the spotlight compared to the past.
- Gartner, a U.S. market research company, selected 'Blockchain commercialization' among the top 10 strategic technology trends in 2020.
- It is predicted that each country will introduce taxes as blockchain transactions in 2023.
- It is estimated that 10% of global gross domestic product (GDP) will be stored with blockchain technology by 2027.

> Google Trend: Blockchain <br/>

![Trend](https://user-images.githubusercontent.com/63955072/122921380-5e477680-d39d-11eb-9609-9d16ea91cacd.png)

## Propose
- We want to logically extract blockchain-related keywords from papers and sites related to blockchain.
- It is planning to find out major technologies through analysis of CPC technologies.
- Through network analysis, we want to analyze the convergence between industrial technologies according to their relevance to blockchain.

## Dataset
- Data Source: USPTO

## Method
- Define Blockchain Keywords in 3 ways
> Technology Keywords: Blockchain technology keywords defined in the paper <br/>

> Trend Keywords: Collection of technical keywords from blockchain-related websites (Binance Academy) <br/>

> Internal Keywords: Keyword collection from blockchain-related patents <br/>

- Define Blockchain in 3 ways
> Core Blockchain: Technology Keywords ∩ Trend Keywords ∩ Internal Keywords <br/>

> Extend Blockchain: Technology Keywords ∩ Trend Keywords + Trend Keywords ∩ Internal Keywords - Core Keywords <br/>

> General Blockchain: Keywords except Core Blockchain and Extend Blockchain. <br/>

## Analysis
- It is analyzed through three defined blockchains.
- It analyzed each blockchain by dividing it into three periods.
> Period 1: 2010.01.01~2012.12.31 <br/>

> Period 2: 2013.01.01~2015.12.31 <br/>

> Period 3: 2016.01.01~2020.06.30 <br/>

> ex) Core Blockchain CPC Network (period1) <br/>

![Core Blockchain CPC Network (period1)](https://user-images.githubusercontent.com/63955072/122924989-58ec2b00-d3a1-11eb-9ae9-06336f25e7d1.png)

> ex) Core Blockchain CPC Matrix (period1) <br/>

![Core Blockchain CPC Matrix (period1)](https://user-images.githubusercontent.com/63955072/122925208-92249b00-d3a1-11eb-9c11-902731cad21f.png)

- Data Analysis
> Core Blockchain: It has found that there is a high connection with network, security, and image fields. <br/>
> Extend Blockchain: It also found that it is related to the electric vehicle industry and the voice analysis technology industry. <br/>
> General Blockchain: It has also found industrial expansion in relation to the areas of healthcare (medicine management, surgical information management), and machine learning. <br/>

## Conclusion
- Through the patent analysis of this study, we were able to identify relatively technical features among the areas that were not mentioned in the blockchain utilization field research.
- Through industrial technology trends and CPC technology trends, we looked at the growth direction of blockchain. 
- We have identified connectivity with healthcare (medication management, information management in surgery), the electric vehicle industry and the 3D printing industry.

## Reference
- http://kiss.kstudy.com/thesis/thesis-view.asp?key=3878951
