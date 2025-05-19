const fs = require('fs');
const { initializeApp, cert } = require('firebase-admin/app');
const { getFirestore } = require('firebase-admin/firestore');
const serviceAccount = require('./serviceAccountKey.json');



initializeApp({
  credential: cert(serviceAccount)
});

const db = getFirestore();
const now = new Date();


const exportData = async () => {
  const usersRef = db.collection('new_users')
  const snapshot = await usersRef.get();

  if (snapshot.empty) {
    console.log('No matching documents.');
    return;
  }

  const data = [];

  let i=1
  snapshot.forEach(doc => {
    const docData = doc.data();
     data.push({ id: doc.id, ...docData });
  });

  const json = JSON.stringify(data, null, 2);
  fs.writeFileSync('./backups/new_users.json', json);
  console.log('Data exported successfully');
};

exportData().catch(console.error);