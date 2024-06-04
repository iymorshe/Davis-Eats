//
//  ContentView.swift
//  Davis Eats
//
//  Created by Iman Morshed on 4/29/24.
//


import SwiftUI

struct ContentView: View {
    var body: some View {
        TabView {
            Home()
            .tabItem {
                Label("Home", systemImage: "house")
                    }
            Calendar()
                .tabItem {
                    Label("Upcoming Meals", systemImage: "calendar")
                }
        }
    }
}
struct Home: View{
    var body: some View {
        Text("Home")
    }
}

struct Calendar: View {
    var body: some View {
        Text("Calendar")
    }
}

#Preview {
    ContentView()
}
