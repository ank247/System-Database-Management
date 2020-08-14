

var Web3 = require("web3");

var url = "https://mainnet.infura.io/v3/60968ff3b2f84a0ebdff7a993f4d080b";

var web3 = new Web3(url);

// Account creation using accounts    
var account = web3.eth.accounts.create();
var account2 = account.address.toLowerCase();
console.log(account2);


// Get all the accounts with the Wallets
var accounts = web3.eth.getAccounts();
console.log(accounts);


// Wallet Account creation using wallet 
var wallet = web3.eth.accounts.wallet.create(2);
var account3 = wallet['0'].address.toLowerCase();
var account4 = wallet['1'].address.toLowerCase();

// Wallets encryption
var encryptKey = web3.eth.accounts.wallet.encrypt('Adu');
var keys = encryptKey.map((accounts) => {
    console.log('0x' + accounts.address.toLowerCase());
});


// Account creation using personal
var personalAccount = web3.eth.personal.newAccount().then((user) => {
    account1 = user.toLowerCase();
    console.log(account1);
});


// Balance check
web3.eth.getBalance(account4, (err, bal) => { console.log(bal); });
web3.eth.getBalance(account2, (err, bal) => { console.log(bal); });



// Notifications on transactions by accounts
var subscription = web3.eth.subscribe('logs', {
    address: wallet['0'].address, topics: ['Adu']
}, function (err, result) {
    console.log(result);
}).on('data', (data) => {
    console.log("Hi!"); // + data);
}).on('connected', function (subscriptionId) {
    console.log(subscriptionId);
}).on('changed', (log) => {
    console.log(log);
});


class TransactionChecker {
    constructor(address) {
        this.web3 = new Web3("http://127.0.0.1:8545"); //"https://mainnet.infura.io/v3/60968ff3b2f84a0ebdff7a993f4d080b");
        this.address = address.toLowerCase();
        this.db = {}
    }

    /* Sample DB
        db = {
            "AAdharNumber":{
                "wallet": Rs. 100,
                'walletAddress':'0xdfkhjgghjhghfgd',
                'etherAmount': 100,
                'privateKey' : PRIVATE_KEY
            }
        }
    */

    async createAccount(aadharNumber) {
        try {
            if (this.db[aadharNumber] == null) {
                this.db[aadharNumber] = {};
                this.db[aadharNumber].wallet = 0;

                // var Person = (function(){
                //     this.counter = 0;
                //     return ()=>{
                //         this.counter++;
                //     }
                // })();
                // var person = new Person;
                // console.log(person.counter);

                // Wallet Account creation using wallet 
                const wallet = this.web3.eth.accounts.wallet.create(1);
                // Wallets encryption
                const encryptKey = this.web3.eth.accounts.wallet.encrypt('Adu');
                this.db[aadharNumber].address = '0x' + encryptKey['0'].address.toLowerCase();
                // await allows to setTickTime()
                this.db[aadharNumber].privateKey = wallet['0'].privateKey;
                // get balance
                let db = this.db;
                let addr = this.db[aadharNumber].address.toLowerCase();
                var bal = this.web3.eth.getBalance(addr, 'latest', function (err, bal) {
                    db[aadharNumber].ether = bal;
                });
                this.db = db;
                console.log(this.db[aadharNumber].ether);
            } else {
                console.log("You have already an account: " + this.db[aadharNumber].address);
            }
        } catch (err) {
            console.error(err);
        }
    }

    async checkBalance(aadharNumber) {
        if(typeof aadharNumber == typeof 890){
           var addr = this.db[aadharNumber].address.toLowerCase();
        }else{
            // if aadharNumber is typeof string, then, it is address provided
            var addr = aadharNumber;
        }
        this.web3.eth.getBalance(addr, 'latest', (err, bal) => {
            console.log("ether on " + addr + " : " + bal + " ETH");
        });
    }
   
    // ether to ether payment
    async moneyTransaction(from, to, val) {
        let transaction = this.web3.eth.sendTransaction({
            from: from.toLowerCase(),
            to: to.toLowerCase(),
            value: val
            // data: data
        });
    }

    async moneyToWalletConversion(address = null, walletAmount) {
        // ether payment to Admin's account
        this.moneyTransaction(address, this.address, walletAmount);
        // ether balance of client
        this.checkBalance(address);
        // ether balance of Admin
        this.checkBalance(this.address);
        //console.log("Hi "+address, this.address, walletAmount);
    }

    // wallet to wallet payment from one client to other
    async walletPayment(fromAadharNumber, toAadharNumber, walletAmount) {
        this.db[fromAadharNumber].wallet -= walletAmount;
        this.db[toAadharNumber].wallet += walletAmount;
    }
    
    // latest or provided blocks' transactions record alongwith timestamp
    async checkBlock() {
        let block = await this.web3.eth.getBlock('latest');
        let number = block.number;
        let transactions = block.transactions;
        //console.log('Search Block: ' + transactions);

        if (block != null && block.transactions != null) {
            for (let txHash of block.transactions) {
                let tx = await this.web3.eth.getTransaction(txHash);
                console.log("from: " + tx.from.toLowerCase() + " to: " + tx.to.toLowerCase() + " value: " + tx.value);
                if (this.address == tx.from.toLowerCase()) {
                    console.log("from: " + tx.from.toLowerCase() + " to: " + tx.to.toLowerCase() + " value: " + tx.value);
                }
            }
        }
    }

    // get logs notifications on data entry, logins or error
    async subscribe(topic) {
        this.subscription = this.web3.eth.subscribe(topic, (err, log) => {
            console.log(log);
        });
    }

    // watching recent activities on transactions
    watchTransactions() {
        console.log("Waiting for pending transactions...");
        let block = this.web3.eth.getBlock('latest');
        let number = block.number;
        let transactions = block.transactions;
        setTimeout(async () => {
            this.subscription.on('data', txHash);
            try {
                let tx = await this.web3.eth.getTransaction(txHash);
                if (tx != null) {
                    console.log(tx.from);
                    if (this.account == tx.from.toLowerCase()) {
                        console.log("from: " + tx.from.toLowerCase() + " to: " + tx.to.toLowerCase() + " value: " + tx.value);
                    }
                }
            } catch (err) {
                console.error(err);
            }
        }, 500);
    }
}

var transactionChecker = new TransactionChecker("0x8b05780f5Fb2E7c267b6941f295F7f3D120D2801");

// multiple transaction records
transactionChecker.createAccount(345654);
transactionChecker.checkBalance(345654);
transactionChecker.createAccount(345654);
transactionChecker.createAccount(345659);
transactionChecker.checkBalance(345659);

// wallet payment from one client to other client 
transactionChecker.walletPayment(345654, 345659, 50);

// ether to ether payment
transactionChecker.moneyTransaction("0x90C5407080ff2e7310EE933c420Ec8ecf3f55924", "0x8b05780f5Fb2E7c267b6941f295F7f3D120D2801", 15000000000);

// money to wallet conversion within same account
transactionChecker.moneyToWalletConversion('0x90C5407080ff2e7310EE933c420Ec8ecf3f55924', 40);
// subscribing for notifications
transactionChecker.subscribe('pendingTransactions');

transactionChecker.watchTransactions();
transactionChecker.checkBlock();
console.log(transactionChecker.db);

