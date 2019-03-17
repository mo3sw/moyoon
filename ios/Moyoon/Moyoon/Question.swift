//
//  Question.swift
//  Moyoon
//
//  Created by Rayan Alajmi on 11/30/18.
//  Copyright © 2018 KFUPM-SWE417. All rights reserved.
//

import Foundation
import UIKit
import Firebase
import FirebaseFirestore

class Question: UIViewController {
    let db = Firestore.firestore()
    override func viewDidLoad() {
        super.viewDidLoad()
        getQuestion()
        updateScore();

    }
    @IBOutlet weak var question: UILabel!
    
    override func viewWillAppear(_ animated: Bool) {
        questionNumberLabel.text = "Question: \(GlobalVariables.questionId)"
        roundNumberLabel.text = "Round: \(GlobalVariables.roundId)"
    }
    
    @IBOutlet weak var questionNumberLabel: UILabel!
    @IBOutlet weak var roundNumberLabel: UILabel!
    
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    
    func getQuestion(){
        

        let docRef = db.collection("Session").document(GlobalVariables.sessionId).collection("Rounds").document(GlobalVariables.roundId).collection("Questions").document(GlobalVariables.questionId)
        
        docRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let q = document.data()!["name"] as! String
                self.question.text = q
                print("Document data: \(q)")
            } else {
                print("Document does not exist")
            }
        }
    }
    
    func updateScore(){
        //
        let docPath = "/Session/\(GlobalVariables.sessionId)/Players/\(GlobalVariables.playerId)/"
        let docRef = db.document(docPath)
        docRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let score = document.data()!["Score"] as! Int
                GlobalVariables.currentScore = score;
                print("Current Score: \(score)")
            } else {
                print("Score not found")
            }
        }
    }
}
