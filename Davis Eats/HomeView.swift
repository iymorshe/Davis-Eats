//
//  HomeView.swift
//  Davis Eats
//
//  Created by Sajed Hussein on 6/19/24.
//

import Foundation
import SwiftUI

struct HomeView: View {
    @State var text: String = ""
    
    var body: some View {
        ZStack {
            VStack{
                VStack{
                    HStack {
                        TextField("Search...", text: $text)
                            .padding(7)
                            .padding(.horizontal, 25)
                            .background(Color(.systemGray6))
                            .cornerRadius(8)
                            .overlay(
                                HStack {
                                    Image(systemName: "magnifyingglass")
                                        .foregroundColor(.gray)
                                        .frame(minWidth: 0, maxWidth: .infinity, alignment: .leading)
                                        .padding(.leading, 8)
                                    
                                    if !text.isEmpty {
                                        Button(action: {
                                            self.text = ""
                                        }) {
                                            Image(systemName: "multiply.circle.fill")
                                                .foregroundColor(.gray)
                                                .padding(.trailing, 8)
                                        }
                                    }
                                }
                            )
                            .padding(.horizontal, 10)
                    }
                    List{
                        CardView()
                        CardView()
                        CardView()
                        CardView()
                    }
                    .frame(minWidth: 400, maxWidth: .infinity)
                    .background(Color.clear)
                    .listStyle(PlainListStyle())
                    
                }
                .background(Color.white)
                .padding()
            }
        }
    }
}

#Preview {
    HomeView()
}
    






