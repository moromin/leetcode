class MyCalendar {
//     List<int[]> books;

//     public MyCalendar() {
//         this.books = new ArrayList<int[]>();
//     }
    
//     public boolean book(int start, int end) {
//         for (int[] book: this.books) {
//             // System.out.println(book[0] + " " + book[1]);
//             if (!(book[1] <= start || end <= book[0])) 
//                 return false;
//         }
//         this.books.add(new int[]{start, end});
//         return true;
//     }
    
    TreeMap<Integer, Integer> calendar = new TreeMap<>();
    
    public MyCalendar() {
        this.calendar.put(Integer.MAX_VALUE, Integer.MAX_VALUE);
    }
    
    public boolean book(int start, int end) {
        Map.Entry<Integer, Integer> pair = this.calendar.higherEntry(start);
        // System.out.println(pair.getKey() + " " + pair.getValue());
        boolean res = end <= pair.getValue();
        if (res)
            this.calendar.put(end, start);
        return res;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */