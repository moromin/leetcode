class MyCalendar {
    List<int[]> books;

    public MyCalendar() {
        this.books = new ArrayList<int[]>();
    }
    
    public boolean book(int start, int end) {
        for (int[] book: this.books) {
            // System.out.println(book[0] + " " + book[1]);
            if (!(book[1] <= start || end <= book[0])) 
                return false;
        }
        this.books.add(new int[]{start, end});
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */