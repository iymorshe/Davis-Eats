//
//  CardView.swift
//  Davis Eats
//
//  Created by Sajed Hussein on 6/19/24.
//
import SwiftUI

struct Card {
    var name: String
    var location : String
    var closingHour : String
}

struct CardView: View {
    var body: some View {
        VStack {
            ZStack(alignment: .bottomLeading) {
                AsyncImage(url: URL(string: "https://housing.ucdavis.edu/_images/dining/silo-restaurants/silo-restaurants-interior-20200720-01.jpg")) { image in
                    image.resizable()
                        .aspectRatio(contentMode: .fill)
                        .frame(width: 340, height: 200)
                        .clipped()
                        .cornerRadius(12)
                } placeholder: {
                    ProgressView()
                        .frame(width: 340, height: 200)
                }
               
                    VStack(alignment: .leading, spacing: 4) {
                        HStack{
                            Text("Silo Market")
                                .font(.headline)
                                .foregroundColor(.black)
                            Spacer()
                            Image(systemName: "star")
                                .foregroundColor(.gray)
                        }
                        
                        Text("Silo")
                            .font(.subheadline)
                            .foregroundColor(.gray)
                        
                        Text("Open until 4:00pm")
                            .font(.caption)
                            .foregroundColor(.green)
                    }
                    .padding()
                    .frame(minWidth: 340, maxHeight: 80, alignment: .leading)
                    .background(Color.white)
            }
    
        }
        .frame(width: 340, height: 200)
        .background(Color.gray.opacity(0.2))
        .cornerRadius(12)
        .shadow(radius: 5)
    }
    
}

struct CardView_Previews: PreviewProvider {
    static var previews: some View {
        CardView()
    }
}
