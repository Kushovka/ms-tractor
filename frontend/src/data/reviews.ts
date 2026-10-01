export type Review = {
  author: string
  rating: number
  date: string
  text: string
}

// These review excerpts belong to the previous dealership and need replacement with M & S reviews.
export const reviews: Review[] = [
  { author: 'K Thomas', rating: 5, date: '1 year ago', text: 'Professional, reliable service, clear updates, and fair pricing.' },
  { author: 'Wanda', rating: 5, date: '7 years ago', text: 'A family run shop with honest people, fair prices, and quality service.' },
  { author: 'Dan Huey', rating: 5, date: '1 year ago', text: 'Bought vehicles here and found the family business wonderful to work with.' },
  { author: 'Adam Cohn', rating: 5, date: '5 years ago', text: 'A great family auto shop with a straightforward, honest owner.' },
  { author: 'Robert Kountz', rating: 5, date: '5 years ago', text: 'Friendly people and reasonable prices.' },
  { author: 'Robin Romanchik', rating: 5, date: '1 year ago', text: 'An honest and very reasonable person.' },
]
