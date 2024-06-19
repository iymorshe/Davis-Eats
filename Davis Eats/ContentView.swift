import SwiftUI

struct ContentView: View {
    
    var body: some View {
        TabView {
            HomeView()
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



struct Calendar: View {
    var body: some View {
        Text("Calendar")
    }
}

#Preview {
    ContentView()
}
