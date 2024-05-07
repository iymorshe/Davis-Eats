  //
//  Davis_EatsApp.swift
//  Davis Eats
//
//  Created by Iman Morshed on 4/29/24.
//

import SwiftUI

@main
struct Davis_EatsApp: App {
    let persistenceController = PersistenceController.shared

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
        }
    }
}
